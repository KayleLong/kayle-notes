#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

length = 5
breadth = 2
area = length * breadth
# 字符串拼接，适用于参数少
print 'Area is', area
# 格式化输出，适用于多参数，类型少
print 'Area is %d' % (area)
# format()输出，适用于多参数，多类型，参数很灵活
print 'Area is {t_area}'.format(t_area=area)

print 'Perimeter is %d' % (2*(length+breadth))
print 'Perimeter is', 2*(length+breadth)
print 'Perimeter is {t_perimeter}'.format(t_perimeter=2*(length+breadth))