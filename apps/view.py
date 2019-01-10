from .models import Demo
from admin import ModelView


class DemoView(ModelView):
    """
    自定义视图
    """
    column_list = (
        "id", "name"
    )

    def __init__(self, **kwargs):
        super(DemoView, self).__init__(Demo, **kwargs)
