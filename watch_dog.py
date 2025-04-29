import time
from time import perf_counter as pc
from typing import Any
import subprocess
import watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import watchdog.events
import datetime
import os
import io
from contextlib import redirect_stdout
        

    
# print("output", output)
os.system("ECHO")
os.system("TITLE Watch_Dog")
os.system("mode con: cols=120 lines=30")
       
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[0;31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
          
class _DuplicateEventLimiter:
    """Duplicate event limiter.

    This class is responsible for limiting duplicated event detection. It works
    by comparing the timestamp of the previous event (if existent) to the
    current one, as well as the event itself. If the difference between the
    timestamps is less than a threshold and the events are the same, the event
    is considered a duplicate.
    """

    _DUPLICATE_THRESHOLD: float = 0.05

    def __init__(self) -> None:
        """Initialize a _DuplicateEventLimiter instance."""
        # Dummy event:
        self._last_event: dict[str, Any] = {
            "time": 0,
            "event": None
        }

    def _is_duplicate(self, event: watchdog.events.FileSystemEvent) -> bool:
        """Determine if an event is a duplicate.

        Args:
            event (watchdog.events.FileSystemEvent): event to check.

        Returns:
            bool: True if the event is a duplicate, False otherwise.
        """
        is_duplicate = (
            pc() - self._last_event["time"] < self._DUPLICATE_THRESHOLD
            and self._last_event["event"] == event
        )

        self._last_event = {
            "time": pc(),
            "event": event
        }

        return is_duplicate

class MyHandler(FileSystemEventHandler, _DuplicateEventLimiter  
                # Inherit the class from the child.
            ):
    def __init__(self) -> None:
        _DuplicateEventLimiter.__init__(self)
        try:
            with open("watch_dog.log", "r") as file:
                path = file.read().split("\n")[-2]
                if ".py" in path:
                    os.system("cls")
                    print(f"{bcolors.OKGREEN}Restore Latest Changed FILE {path} {bcolors.ENDC}")
                    print(f"{bcolors.OKGREEN}... Running Now ... \n__________________________________\n{bcolors.ENDC}")
                    self.solve(path)
        except FileNotFoundError:
            pass
    def store_last_runtime_path(self, path):
        with open("watch_dog.log", "a") as file:
            file.write(path+"\n")
    
    def run_file_and_get_output(code_as_str: str):
        with open("C:/Users/admin/OneDrive - VINACADEMY LLC/Desktop/watch_dog.py", mode="r") as file:
            x = file.read()
            print(x)
            
        with io.StringIO() as buf, redirect_stdout(buf):
            output = buf.getvalue()

       
    
    def solve(self, path):
        try:
            # proc = subprocess.Popen([f'''python {path} arg1 arg2 arg3 arg4'''], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            proc = subprocess.Popen(['''(Measure-Command { python '''+path+''' | Out-Default }).ToString()'''], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            
            start_time = time.perf_counter()
            output = proc.communicate(timeout = 1)[0].decode("utf-8")
            end_time = time.perf_counter()
            returncode = proc.returncode
            runtime_status = 0
        except subprocess.TimeoutExpired:
            output = " "
            runtime_status = 1
            returncode = 0

            
        if returncode == 1:
            # os.system("color 04")
            print(f"{bcolors.FAIL}{output}{path.split("\\")[-1]}{bcolors.ENDC}\n")
            print(f"{bcolors.WARNING}Error: Error On Interpreting File {path.split("\\")[-1]}{bcolors.ENDC}")
        elif len(output) == 0:
            # os.system("color 03")
            print(f"{bcolors.WARNING}{output}{path.split("\\")[-1]}{bcolors.ENDC}")
            print(f"{bcolors.WARNING}Warning: No Output Received From {path.split("\\")[-1]}{bcolors.ENDC}")
        else:
            print(output)
            print()
            if runtime_status == 0:
                elapsed_time = end_time - start_time
                elapsed_time = elapsed_time * 1000
                elapsed_time = elapsed_time - 25
                print(f"{bcolors.OKGREEN}Excuted Successfully In {elapsed_time:.0f}ms. Have A Good Day Sir! {bcolors.ENDC}")
            else:
                print(f"{bcolors.WARNING}Error: Timeout, {path.split("\\")[-1]} Takes More Than 1 Second To Run. {bcolors.ENDC}")
                
            # os.system("color 07")
            
    def on_modified(self, event):
        os.system("cls")
        print(f"{bcolors.OKGREEN}Modify Detected On {datetime.datetime.now().strftime("%I:%M%p")} FILE {path} {bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}... Running Now ... \n__________________________________\n{bcolors.ENDC}")
        
        if self._is_duplicate(event):
            # Do whatever if event is duplicate.
            return  # Or just stop execution of the method.
          
        assert event.is_directory == False
        path = event.src_path
        event = str(event)
        assert "FileModifiedEvent" in event
        
        self.solve(path)
        self.store_last_runtime_path(path)

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='C:/Users/admin/OneDrive - VINACADEMY LLC/Desktop/Lab_Vinuni', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    
# from __future__ import print_function
# from time import perf_counter as pc
# from typing import Any
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# import traceback
# import threading
# import watchdog
# import datetime
# import ctypes
# import time
# import sys
# import os
# import io
# import watchdog.events
# from contextlib import redirect_stdout
# import multiprocessing

# def worker(input_queue, output_queue):
#     """
#     Function to run in a separate process.
#     It processes input from the input_queue and sends the result to the output_queue.
#     """
#     input_str = input_queue.get()
#     output_str = f"Processed: {input_str}"  # Perform the processing here
#     output_queue.put(output_str)
# def start_process():
#     """
#     Initializes the input and output queues and starts the process.
#     Returns the process object and the queues.
#     """
#     input_queue = multiprocessing.Queue()
#     output_queue = multiprocessing.Queue()

#     process = multiprocessing.Process(target=worker, args=(input_queue, output_queue))
#     process.start()

#     return process, input_queue, output_queue
# def run_in_process(input_str):
#     """
#     Main function to send a string input to a separate process and receive the output.
#     """
#     process, input_queue, output_queue = start_process()

#     # Send input and get output
#     input_queue.put(input_str)
#     result = output_queue.get()

#     # Wait for the process to finish
#     process.join()

#     return result

# exec_thread_id = None
# last_file_str = None

# def ctype_async_raise():
#     global exec_thread_id
#     target_tid = exec_thread_id
#     exception = NotImplementedError
#     ret = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(target_tid), ctypes.py_object(exception))
#     # ref: http://docs.python.org/c-api/init.html#PyThreadState_SetAsyncExc
#     if ret == 0:
#         raise ValueError("Invalid thread ID")
#     elif ret > 1:
#         # Huh? Why would we notify more than one threads?
#         # Because we punch a hole into C level interpreter.
#         # So it is better to clean up the mess.
#         ctypes.pythonapi.PyThreadState_SetAsyncExc(target_tid, NULL)
#         raise SystemError("PyThreadState_SetAsyncExc failed")
# def quit_function(fn_name):
#     # print to stderr, unbuffered in Python 2.
#     sys.stderr.flush() # Python 3 stderr is likely buffered.
#     # thread.interrupt_main() # raises KeyboardInterrupt
#     ctype_async_raise()
# def exit_after(s):
#     '''
#     use as decorator to exit process if 
#     function takes longer than s seconds
#     '''
#     def outer(fn):
#         def inner(*args, **kwargs):
#             timer = threading.Timer(s, quit_function, args=[fn.__name__])
#             timer.start()
#             try:
#                 result = fn(*args, **kwargs)
#             finally:
#                 timer.cancel()
#             return result
#         return inner
#     return outer
# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKCYAN = '\033[96m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[0;31m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
# class _DuplicateEventLimiter:
#     """Duplicate event limiter.

#     This class is responsible for limiting duplicated event detection. It works
#     by comparing the timestamp of the previous event (if existent) to the
#     current one, as well as the event itself. If the difference between the
#     timestamps is less than a threshold and the events are the same, the event
#     is considered a duplicate.
#     """

#     _DUPLICATE_THRESHOLD: float = 0.05

#     def __init__(self) -> None:
#         """Initialize a _DuplicateEventLimiter instance."""
#         # Dummy event:
#         self._last_event: dict[str, Any] = {
#             "time": 0,
#             "event": None
#         }

#     def _is_duplicate(self, event: watchdog.events.FileSystemEvent) -> bool:
#         """Determine if an event is a duplicate.

#         Args:
#             event (watchdog.events.FileSystemEvent): event to check.

#         Returns:
#             bool: True if the event is a duplicate, False otherwise.
#         """
#         is_duplicate = (
#             pc() - self._last_event["time"] < self._DUPLICATE_THRESHOLD
#             and self._last_event["event"] == event
#         )

#         self._last_event = {
#             "time": pc(),
#             "event": event
#         }

#         return is_duplicate
# class MyHandler(FileSystemEventHandler, _DuplicateEventLimiter):
#     def __init__(self) -> None:
#         _DuplicateEventLimiter.__init__(self)
        
#         os.system("ECHO")
#         os.system("TITLE Watch_Dog")
#         os.system("mode con: cols=120 lines=30")
        
#         try:
#             with open("watch_dog.log", "r") as file:
#                 path = file.read().split("\n")[-2]
#                 if ".py" in path:
#                     os.system("cls")
#                     print(f"{bcolors.OKGREEN}Restore Latest Changed FILE {path} {bcolors.ENDC}")
#                     print(f"{bcolors.OKGREEN}... Running Now ... \n__________________________________\n{bcolors.ENDC}")
#                     self.solve(path)
#         except FileNotFoundError:
#             pass
            
#     def store_last_runtime_path(self, path):
#         with open("watch_dog.log", "a") as file:
#             file.write(path+"\n")
    
#     def run_file_and_get_output(code_as_str: str):
#         pass

#     def solve(self, path):
#         global last_file_str, exec_thread_id
        
#         @exit_after(1)
#         def temp():
#             exec(code_as_str)
            
#         with open(path, mode="r") as file:
#             code_as_str = file.read()
#             if code_as_str == last_file_str:
#                 return
        
#         with io.StringIO() as buf, redirect_stdout(buf):
#             try:
#                 start_time = time.perf_counter()
#                 runtime_status = 0
#                 exec_thread_id = threading.current_thread().ident
#                 temp()
#                 end_time = time.perf_counter()
#                 output = buf.getvalue()
#                 returncode = 0
#                 last_file_str = code_as_str
                
#             except NotImplementedError:
#                 returncode = 0
#                 runtime_status = 1
#                 output = " "

#             except Exception:
#                 returncode = 1
#                 output = traceback.format_exc()
        
#         if returncode == 1:
#             # os.system("color 04")
#             print(f"{bcolors.FAIL}{output}{path.split("\\")[-1]}{bcolors.ENDC}\n")
#             print(f"{bcolors.WARNING}Error: Error On Interpreting File {path.split("\\")[-1]}{bcolors.ENDC}")
#         elif len(output) == 0:
#             # os.system("color 03")
#             print(f"{bcolors.WARNING}{output}{path.split("\\")[-1]}{bcolors.ENDC}")
#             print(f"{bcolors.WARNING}Warning: No Output Received From {path.split("\\")[-1]}{bcolors.ENDC}")
#         else:
#             print(output)
#             print()
#             if runtime_status == 0:
#                 elapsed_time = end_time - start_time
#                 elapsed_time = elapsed_time * 1000
#                 print(f"{bcolors.OKGREEN}Excuted Successfully In {elapsed_time:.2f}ms.{bcolors.ENDC}")
#             else:
#                 print(f"{bcolors.WARNING}Error: Timeout, {path.split("\\")[-1]} Takes More Than 1 Second To Run. {bcolors.ENDC}")
            
#     def on_modified(self, event):
#         if self._is_duplicate(event):
#             # Do whatever if event is duplicate.
#             return  # Or just stop execution of the method.
          
#         assert event.is_directory == False
#         path = event.src_path
#         event = str(event)
#         assert "FileModifiedEvent" in event
        
#         os.system("cls")
#         print(f"{bcolors.OKGREEN}Modify Detected On {datetime.datetime.now().strftime("%I:%M%p")} FILE {path} {bcolors.ENDC}")
#         print(f"{bcolors.OKGREEN}... Running Now ... \n__________________________________\n{bcolors.ENDC}")
        
#         self.solve(path)
#         self.store_last_runtime_path(path)

# if __name__ == "__main__":
    
#     event_handler = MyHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path='C:/Users/admin/OneDrive - VINACADEMY LLC/Desktop/Lab_Vinuni', recursive=False)
#     observer.start()

#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()