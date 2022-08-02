from PyMacAdmin.crankd.handlers import BaseHandler

class MountManager(BaseHandler):
    def onNSWorkspaceDidMountNotification_(self, aNotification):
        path = aNotification.userInfo()['NSDevicePath']
        self.logger.info(f"Mount: {path}")

    def onNSWorkspaceDidUnmountNotification_(self, aNotification):
        path = aNotification.userInfo()['NSDevicePath']
        self.logger.info(f"Unmount: {path}")

