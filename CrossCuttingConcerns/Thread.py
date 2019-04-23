# ======================================================================================================================
# importing external modules
from threading import Thread as BaseThread

# ======================================================================================================================
# importing internal modules
from CrossCuttingConcerns.App import App


# ======================================================================================================================
# class Thread : Derived from App and the Python internal Thread (as BasedThread alias here). Implement generic methods
#                for a thread object. The only thing that remains on client side are client specfic application logic /
#                orchestration / etc. Thread are actually derived from App object and should be conceptually treated by
#                client side as mini sub-program, with their own mini sub-module.
class Thread(App, BaseThread):

    # ==================================================================================================================
    # Class Methods
    # ==================================================================================================================
    # __init__ : Constructor for a new app object, basically redirecting to super class the construction
    def __init__(self, p_str_thread_name):
        BaseThread.__init__(self, name=p_str_thread_name, target=Thread._start, args=([self]))
        App.__init__(self, p_str_thread_name)

    # ==================================================================================================================
    # load :    To be implemented client-side to perform all sort of loading and creating modules
    def load(self):
        raise NotImplementedError("Subclass must implement abstract method")

    # ==================================================================================================================
    # event_one_loop :
    def event_one_loop(self, param1=None):
        self.on_manage()

    # ==================================================================================================================
    # _start : Our own private internal start that will be the hook for the Python BaseThread. Not to be confused with
    #           the start function that is to be call client side to initiated the thread.
    def _start(self, param1=None):
        self.is_running = True
        self.load()
        self.main()
