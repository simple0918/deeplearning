import tensorflow as tf

# 在变量空间one下创建名字为a的变量
with tf.variable_scope("one"):
    a = tf.get_variable("a", [1], initializer=tf.constant_initializer(1.0))
# constant_initializer 将变量初始化为给定常亮
# 在生成上下文管理器时，将reuse参数设置为True，这样get_variable()函数将直接获取
# 已经声明的变量(而且是只能获取已经声明的变量)
with tf.variable_scope("one", reuse=True):
    a2 = tf.get_variable("a", [1])
    print(a.name, a2.name)
    # 输出为one/a:0 one/a:0

# 将参数reuse设置为True时，由于get_variable()函数只能获取已经创建过的变量，且
# 命名空间True中并没有创建过那么属性为a的变量，所以下面这段代码将会报错
# ValueError: Variable two/a does not exist, or was not created with
# tf.get_variable(). Did you mean to set reuse=None in VarScope?
# 当variable_scope（）函数使用reuse=True 参数生成上下文管理器时，这个上下文管理器内的所有get_variable（）函数会
# 直接获取name 属性相同的己经创建的变量。如果变量不存在，则get_variable（）函数会报错
with tf.variable_scope("two", reuse=True):
    v1 = tf.get_variable("a", [1])
