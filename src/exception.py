import sys 

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() #excecutaion info, last info give exe_tb (on which file, on which line number, etc)

    filename = exc_tb.tb_frame.f_code.co_filename #excectution tab has tb_frame which has f_code which has co_filename
    lineno = exc_tb.tb_lineno #excecutaion tab has tb_lineno which has line number

    error_message = f"error occured in python script name [{filename}] line number [{lineno}] error message [{error}]"

    # error_message = "error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    #     filename,lineno,str(error)
    # )
    return error_message

    

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
