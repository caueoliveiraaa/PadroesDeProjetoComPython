from abc import ABC, abstractmethod


# Abstract class or model class
class AbstractClass(ABC):
    # Routine = Methods called to run all the steps of the process
    def template_method(self):
        self.common_step1()
        self.specialized_step2()
        self.common_step3()
        
    # This method will run for all subclasses
    def common_step1(self):
        print("AbstractClass: Performing common step 1")
        
    # This method needs to be modified by subclasses
    @abstractmethod
    def specialized_step2(self):
        ...
        
    # This method will run for all subclasses
    def common_step3(self):
        print("AbstractClass: Performing common step 3")
        
# Creating a subclass for the class above
class ConcreteClass(AbstractClass):
    # Adapting the abstract method
    def specialized_step2(self):
        print("ConcreteClass: Performing specialized step 2")
        
def main():
    # Instantiating an object of the class and running the routine
    concrete_object = ConcreteClass()
    concrete_object.template_method()
    
    
if __name__ == "__main__":
    # Run template method
    main()