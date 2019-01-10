# author:师仁杰


def create_mark(title, method):
    content = """
    # %s
    ----

    `%s` **https://www.ultrabear.com.cn/docs/receive/**

    输入

    ```json
    {
        "coupon": "gFwwa",
        "staff": "zs",
        "username": "zhangsan",
        "phone": "18700790000"
    }
    ```

    成功输出

    ```json
    {
            "code": 0,
            "data": "领取成功",
            "msg": "请求成功"
        }

    ```

    失败回调

    ```json

    {
            "code": 1,
            "data": "",
            "msg":"课程领取满额"
    }

    ```


    """
    content = content % (title, method)
    return content



