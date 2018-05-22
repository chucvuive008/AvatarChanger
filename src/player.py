from transformer import*


class Player:
    def __init__(self, avatar):
        self.current_avatar = avatar

    def perform_action(self):
        self.current_avatar.action()

    def up_from(self, transformer):
        self.current_avatar = transformer.transform_up(self.current_avatar)

    def down_from(self, transformer):
        self.current_avatar = transformer.transform_down(self.current_avatar)
