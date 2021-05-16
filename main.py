#!/usr/bin/env python
# coding=utf-8

# import markdowm
import time

from datetime import datetime, timedelta




def week_of_year():
    """
    获取当前是全年的第几周
    补丁：由于2021年周报前边时间算错，周相差2天，故特殊处理
    
    """
    year = time.strftime("%Y")
    weekly = int(time.strftime("%W"))
    if year == "2021":
        weekly += 2
    return year, str(weekly)



def date_list():
    """
    本周日期列表
    """
    now = datetime.now()
    this_week_start = now - timedelta(days=now.weekday())
    this_week_end = now + timedelta(days=6-now.weekday())
    return [this_week_start+timedelta(days=i) for i in range(5)]


def write_unordered_list(f, template=None):
    """param: <class '_io.TextIOWrapper'>"""
    if not template:
        template = ""
    f.write("* %s\n" %template)
    f.write("* %s\n" %template)
    f.write("\n")


def write_template():
    year, weekly = week_of_year()
    filename = "./data/%s_%s.md" % (year, weekly)

    this_week_date_list = date_list()
    with open(filename, "w") as f:
        f.write("# %s年第%s周\n" % (year, weekly))

        f.write("### 上周总结：\n")
        write_unordered_list(f, template="【0%-100%】")
        f.write("### 下周计划：\n")
        write_unordered_list(f, template="【0%-100%】")
        f.write("\n\n")

        for i in this_week_date_list:
            f.write("%s.%s.%s 今日工作\n" % (i.year, i.month, i.day))
            write_unordered_list(f)


def main():
    write_template()
    

if __name__ == "__main__":
    main()

