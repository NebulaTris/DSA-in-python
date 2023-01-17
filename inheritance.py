#Single Inheritance

classParentClass: deffeature_1(self):
    print('feature_1 from ParentClass is running...')
    deffeature_2(self):
      print('feature_2 from ParentClass is running...')
      classChildClass(ParentClass): 
        deffeature_3(self):
          print('feature_3 from ChildClass is running...') 
          obj = ChildClass()
          obj.feature_1() 
          obj.feature_2()
          obj.feature_3()
          
 #Multiple Inheritance
classParentClass_1:
  deffeature_1(self):
    print('feature_1 from ParentClass_1 is running...')
classParentClass_2:
  deffeature_2(self):
    print('feature_2 from ParentClass_2 is running...')
classChildClass(ParentClass_1, ParentClass_2): deffeature_3(self):
    print('feature_3 from ChildClass is running...')
    obj = ChildClass()
    obj.feature_1() 
    obj.feature_2() 
    obj.feature_3()
    
#Hierarchial Inheritance
classParentClass_1: 
  deffeature_1(self):
    print('feature_1 from ParentClass_1 is running...') 
classParentClass_2:
  deffeature_2(self):
    print('feature_2 from ParentClass_2 is running...')
classChildClass(ParentClass_1, ParentClass_2): 
  deffeature_3(self):
  print('feature_3 from ChildClass is running...')
  obj = ChildClass() 
  obj.feature_1() 
  obj.feature_2() 
  obj.feature_3()
