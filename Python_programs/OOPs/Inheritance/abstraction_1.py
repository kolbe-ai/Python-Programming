"""
(Abstraction: Interface) [PDF Q57] Define an interface-style Notification with send(msg). Implement EmailNotification and SMSNotification.
"""

from abc import ABC,abstractmethod
class Notification(ABC):
  @abstractmethod
  def send(msg):
    pass


class SMSNotification(Notification):
  def send(self,msg):
    print(f"[From SMS]: {msg}")

class EmailNotification(Notification):
  def send(self,msg):
    print(f"[From Email]: {msg}")


e = EmailNotification()
s = SMSNotification()
e.send("Hello EMAIL")
s.send("Hello from SMS")