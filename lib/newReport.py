import os


def new_report(testreport):
    """
    生成最新的测试报告文件
    :param testreport:
    :return:返回文件
    """
    # 获取param:testreport目录下的全部文件, 按日期排序
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    return file_new


if __name__ == '__main__':
    print(new_report(r'D:/1dth/Project/dth_api\report'))
