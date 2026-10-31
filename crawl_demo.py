# -*- coding: utf-8 -*-
"""
爬虫示例：抓取 2026 年中国移动江西公司的招标采购公告
======================================================
运行方式：python crawl_demo.py
输出文件：jx_bidding.csv

涉及的知识点（方括号里的编号对应下面的代码段）：
    [1] import 导入库
    [2] 常量 / 配置集中管理
    [3] requests.post() 发送 JSON 请求
    [4] resp.json() 把响应解析成字典
    [5] dict.get() 安全取值（字段缺失也不报错）
    [6] while / for / if 循环与条件判断
    [7] pandas to_csv 导出 CSV
    [8] try / except 异常捕获
"""

# ========== [1] 导入库 ==========
import requests      # HTTP 客户端，相当于在程序里发浏览器请求
import pandas as pd  # 数据处理库，用来把结果导成 CSV
import time          # 控制请求间隔，别把人家服务器打崩
import urllib3       # 用来屏蔽 SSL 安全警告

# ========== SSL 兼容补丁 ==========
# 这个老站点用的是旧版 TLS 协商方式，Python 3.13 默认已禁用，
# 所以这里自定义一个适配器，允许和老服务器握手。
import ssl
from requests.adapters import HTTPAdapter

class LegacySSLAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        ctx = ssl.create_default_context()
        ctx.options |= 0x4   # OP_LEGACY_SERVER_CONNECT，允许老式 TLS 握手
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        kwargs["ssl_context"] = ctx
        return super().init_poolmanager(*args, **kwargs)

# 顺便关掉"不安全请求"的警告提示
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 建一个带旧版 SSL 适配器的会话，后面所有请求都复用它
session = requests.Session()
session.mount("https://", LegacySSLAdapter())

# ========== [2] 配置区 ==========
API_URL = "https://b2b.10086.cn/api-b2b/api-sync-es/white_list_api/b2b/publish/queryList"

# 请求头：后端接口要求的上下文头（processInstId / userLoginName）不能少，
# 少了会返回"单据数据处理异常"
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Referer": "https://b2b.10086.cn/",
    "processInstId": "-1",
    "userLoginName": "-1",
}

TARGET_YEAR = "2026"
TARGET_COMPANY = "\u6c5f\u897f"   # 用 unicode 转义写"江西"，避免文件编码问题
                                  # \u6c5f = 江，\u897f = 西


def fetch_page(page_num):
    """抓取一页数据，返回列表（每个元素是一条公告的字典）。"""
    # ========== [3] POST 请求，请求体是 JSON ==========
    payload = {
        "name": "",
        "publishType": "PROCUREMENT",   # 采购类公告
        "companyType": "",
        "size": 50,                     # 每页 50 条
        "current": page_num,            # 第几页
        "sfactApplColumn5": "PC",
    }

    resp = session.post(API_URL, headers=HEADERS, json=payload, timeout=30)

    # ========== [8] 异常处理 ==========
    # 如果 HTTP 状态码是 4xx / 5xx，这里会抛出异常，被上层的 try/except 接住
    resp.raise_for_status()

    # ========== [4] 解析 JSON ==========
    data = resp.json()   # 把服务器返回的 JSON 字符串变成 Python 字典

    if data.get("code", -1) != 0:
        print(f"  [警告] 接口返回异常：{data}")
        return []

    return data["data"]["content"]


def is_target(item):
    """判断这条公告是不是"江西 + 2026年"的."""
    # ========== [5] 安全取值 ==========
    # 用 .get() 而不是 ["key"]：字段不存在时返回空字符串，不会报 KeyError
    company = item.get("companyTypeName", "")
    date = item.get("publishDate", "")

    # ========== [6] 条件判断 ==========
    return company == TARGET_COMPANY and date.startswith(TARGET_YEAR)


def main():
    print(f"开始抓取 {TARGET_YEAR} 年江西的招标采购公告...")

    rows = []          # 存放所有命中的记录
    page = 1
    max_pages = 50     # 安全上限，防止死循环

    # ========== [6] while 翻页 ==========
    while page <= max_pages:
        print(f"  正在抓第 {page} 页...", end=" ")

        try:
            items = fetch_page(page)
        except Exception as e:
            print(f"失败：{e}")
            page += 1
            continue

        if not items:
            print("本页为空，结束。")
            break

        # ========== [6] for + 过滤 ==========
        for item in items:
            if is_target(item):
                rows.append({
                    "pub_time": item.get("publishDate"),
                    "type":     item.get("publishOneType_dictText"),
                    "project":  item.get("name"),
                })

        print(f"本页 {len(items)} 条，累计江西 2026 年：{len(rows)} 条")

        # 提前结束：列表按时间倒序，最后一条都早于 2026 年了，后面只会更早
        last_date = items[-1].get("publishDate", "")
        if last_date < "2026-01-01":
            print("已到 2025 年数据，提前结束。")
            break

        page += 1
        time.sleep(0.3)   # 每次请求间隔 0.3 秒，礼貌一点


    # ========== [7] pandas 导出 CSV ==========
    if rows:
        df = pd.DataFrame(rows)
        # 改成中文表头；utf-8-sig 编码保证 Excel 打开不乱码
        df.columns = ["发布时间", "公告类型", "项目名称"]
        df.to_csv("jx_bidding.csv", index=False, encoding="utf-8-sig")
        print(f"\n完成！共 {len(rows)} 条，已保存到 jx_bidding.csv")
    else:
        print("\n没有匹配到数据，检查一下网络或接口。")


# 只有直接运行这个文件时才执行 main()；被别的文件 import 时不执行
if __name__ == "__main__":
    main()
