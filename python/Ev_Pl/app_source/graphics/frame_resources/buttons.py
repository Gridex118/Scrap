# Graphics for Event Planner - (Button)

# _________________________________________ Imports

from app_source.graphics.frame_resources.bases import MyButton, MyBlueButton

# _________________________________________ Classes


class CreateAccButton(MyBlueButton):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(text='Add Account',command=self.parent.crAcc)


class AccNextButton(MyBlueButton):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(text='Next',command=self.parent.nextPage)


class AccFinishButton(MyBlueButton):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(text='Finish',command=self.parent.register)


class LoginButton(MyBlueButton):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(text='Log In',command=self.parent.login)


class LogoutButton(MyButton):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(width=18,height=2)
        self.config(text='Log Out',command=self.parent.logout)


class DeleteAccButton(MyButton):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(width=18,height=2)
        self.config(activebackground='#FE002A')
        self.config(text='Delete Account',command=self.parent.deleteAccount)

    def on_entering(self,event):
        self.config(bg='#FE002A', fg='#FEFEFE')


class UpdateAccButton(MyBlueButton):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(width=17)
        self.config(text='Update Account', command=self.update_acc)

    def update_acc(self):
        self.parent.app.render_error_popup('Not Implemented')


class MySqlPassEnterButton(MyBlueButton):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(text='Enter', command=self.parent.enterPass)


class MySqlPassCancelButton(MyBlueButton):

    def __init__(self, parent):
        super().__init__(parent)
        self.config(text='Cancel', command=self.parent.app.shutdown)


class OkButton(MyBlueButton):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(text='Ok',command=self.parent.parent.destroy)


class CardButton(MyButton):

    def __init__(self, parent, operation, card_type='variable'):
        super().__init__(parent)
        self.card_type = card_type
        self.operation = operation.lower()
        self.config(text=operation,
                    width=20,
                    bg='#FAFAFA',
                    command=self.on_click)

    def on_click(self):
        if self.operation in ('next', 'prev'):
            max_index = len(self.parent.cards) - 1
            if self.operation == 'next':
                self.parent.current_card.index += 1
                if self.parent.current_card.index > max_index:
                    self.parent.current_card.index = 0
            elif self.operation == 'prev':
                self.parent.current_card.index -= 1
                if self.parent.current_card.index < 0:
                    self.parent.current_card.index = max_index
        elif self.operation == 'add':
            self.parent.app.render_card_editor(self.card_type)


class SpecificCardButton(CardButton):

    def __init__(self, parent, operation):
        super().__init__(parent, operation)
        self.config(text=operation, width=30)
        if operation == 'delete':
            self.config(activebackground='#FE002A')

    def on_click(self):
        card = self.parent.current_card
        if self.operation == 'delete':
            self.parent.app.render_card_editor()
        elif self.operation == 'edit':
            self.parent.app.render_card_editor()

    def on_entering(self,event):
        if self.operation == 'delete':
            self.config(bg='#FE002A', fg='#FEFEFE')
        else:
            super().on_entering(event)


class SaveCardValuesButton(MyBlueButton):

    def __init__(self, parent):
        super().__init__(parent)
        self.config(text='Add', command=parent.feed_values_to_system)


class DiscardCardValuesButton(MyBlueButton):

    def __init__(self, parent):
        super().__init__(parent)
        self.config(activebackground='#FE002A')
        self.config(text='Discard', command=parent.shutdown)

    def on_entering(self,event):
        self.config(bg='#FE002A')

# __________________________________________________
