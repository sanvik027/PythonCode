import logging

logging.basicConfig(level= logging.DEBUG,filename="../Logs/demologs.log",filemode='a')
class DemoLogging:
    def add_nums(self,a,b):
        return a+b

    def sub_nums(self,a,b):
        return a-b

    def mul_nums(self,a,b):
        return a *b

    def div_nums(self,a,b):
        try:
            if b >0:
                return a/b
            else:
                raise ValueError("The denominator must be greater than 0")
        except ZeroDivisionError as e:
            print(f"Error: Division by zero is not allowed. Details: {e}")
        except ValueError as ve:
            print(f"Error: {ve}")

dl = DemoLogging()
sum_results = dl.add_nums(12,25)
logging.debug("debug: addition of numbers is: {}".format(sum_results))
sub_results = dl.sub_nums(51,14)
logging.info("info: subtraction of numbers is: {}".format(sub_results))
mul_results = dl.mul_nums(30,54)
logging.warning("warning: multiplications of numbers is: {}".format(mul_results))
div_results = dl.div_nums(50,5)
logging.error("error: divison of numbers is: {}".format(div_results))