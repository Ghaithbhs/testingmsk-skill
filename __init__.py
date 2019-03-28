from mycroft import MycroftSkill, intent_file_handler


class Testingmsk(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('testingmsk.intent')
    def handle_testingmsk(self, message):
        self.speak_dialog('testingmsk')


def create_skill():
    return Testingmsk()

