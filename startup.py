import sys

import servicemanager
import win32event
import win32service
import win32serviceutil

from hal_hw_emu import __main__ as main


class Service(win32serviceutil.ServiceFramework):
    _svc_name_ = "halhwemu"
    _svc_display_name_ = "Redbox Hardware Emulator"

    def __init__(self, args):
        super().__init__(args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        main.stop()

    def SvcDoRun(self):
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE, servicemanager.PYS_SERVICE_STARTED, (self._svc_name_, "")
        )
        try:
            servicemanager.LogInfoMsg("Starting main loop.")
            main.main()
            servicemanager.LogInfoMsg("Waiting for stop event.")
            win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)
        except Exception as e:
            servicemanager.LogErrorMsg(f"Service encountered an error: {e}")


if __name__ == "__main__":
    win32serviceutil.HandleCommandLine(Service)
