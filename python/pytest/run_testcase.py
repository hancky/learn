import pytest

# https://blog.csdn.net/chuntingting/article/details/127192385
if __name__ == '__main__':
    # 打印详细信息
    pytest.main(['-vs', 'testcase/calSum/test_calSum.py'])
    
    # 失败2个用例就退出，如果是1个，可直接用x参数
    # pytest.main(['--maxfail=2', 'testcase/test_calSum.py'])

    # 生成报告，会报错，暂时还没有解决
    # pytest.main(['-vs', '-–html=./report/report.html', 'testcase/test_calSum.py'])