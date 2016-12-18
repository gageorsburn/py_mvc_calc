from calc import Calculate
from calc import Operation
from view import View

view = View()
calc = Calculate()

calc.set_output = view.set_output

view.number_event = calc.append
view.clear_event = calc.clear
view.operation_event = calc.set_operation
view.equal_event = calc.do_operation

view.init_components()

view.window.mainloop()
