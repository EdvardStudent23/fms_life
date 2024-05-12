'''
The module represents the life of CS student
using FMS
'''
import random

def step(fn):
    def wrapper(*args, **kwargs):
        v = fn(*args, **kwargs)
        v.send(None)
        return v
    return wrapper

class StudentLifeFSM:
    '''
    A class represents a life of a student
    '''
    def __init__(self):
        a1 = 'Цей крок пропускається, адже для цієї цифри не існує переходу.'

        self.sleeping = self._create_sleeping()
        self.alarm_night = self._alarm_night()
        self.studying = self._create_studying()
        self.eating = self._create_eating()
        self.wakeup = self._create_wakeup()
        self.relax = self._create_relax()
        
        self.current_state = self.sleeping

        self.feel = True
        self.alarm = False 
        
    def send(self, activity):
        '''
        Send a new value for yeild
        '''
        try:
            self.current_state.send(activity)
        except StopIteration:
            self.stopped = True

    @step
    def _create_sleeping(self):
        '''
        represents sleeping
        '''
        while True:
            activity = yield
            if random.random() > 0.5 and self.alarm is False:
                print('"Увага! Повітряна тривога! Пройдіть в укриття!" - той самий голос\
пана Романа зі стелі посеред ночі.')
                print('Ааа!!! Знову москалі не дають спати! Так не хочу в той підвал\
 спускатися >:(')
                self.current_state = self.alarm_night
                self.alarm = True

            elif activity == '1':
                print('Посплю ще трохи, нічого мені не станеться...')
                print('Z-z-z-z')
                self.feel = True
                self.current_state = self.current_state
            elif activity == '2':
                print('Незабаром вставати треба! Такі гарні сни снилися.')
                self.feel = False
                self.current_state = self.wakeup
            else:
                continue

    @step
    def _alarm_night(self):
        '''
        represents alarm
        '''
        while True:
            activity = yield
            if activity == '1':
                print("Та я в принцпипі і так в укритті... (накрився ковдрою)")
                self.current_state = self.sleeping
            elif activity == '2':
                print('Збираюся і йду в підвал')
                self.feel = False
                self.current_state = self.wakeup
            else:
                continue

    @step
    def _create_eating(self):
        '''
        represents eating
        '''
        while True:
            activity = yield
            if random.random() > 0.3:
                print('Повітряна тривога - трапезна зачинена. Жах!')
                print('Йду Ютуб подивлюся, почекаю до відбою.')
                self.current_state = self.relax
            if activity == '1':
                print('Як смачно! Візьму добавку.')
                self.current_state = self.current_state
            elif activity == '2':
                print('О-о! Тепер можна і повчитись!')
                self.current_state = self.studying
            else:
                continue
                

    @step
    def _create_studying(self):
        '''
        represents studying
        '''
        while True:
            activity = yield
            if activity == '1':
                print('Йду щось перекушу, а то зовсім думати не можу.')
                self.current_state = self.eating
            elif activity == '2':
                print('А-а-о-о-у... Так хочу спати...')
                self.current_state = self.sleeping
            elif activity == '3':
                print('Так, тепер варто закрити інший дедлайн\
(Продовжую вчитися)')
                self.current_state = self.studying
            elif activity == '4':
                print('Йду погуляю чи пограю в щось. Вже змучився\
 від того навчання')
                self.current_state = self.relax
            else:
                continue

    @step
    def _create_relax(self):
        '''
        represents relax
        '''
        while True:
            activity = yield
            if activity == '1':
                print("Та сьогодні вже нічого не робитиму. Краще гідно посплю.")
                self.current_state = self.sleeping
            elif activity == '2':
                print('Знову до навчання!')
                self.current_state = self.studying
            else:
                continue

    @step
    def _create_wakeup(self):
        '''
        represents wakeup
        '''
        while True:
            activity = yield
            if random.random() > 0.3:
                print('Хочу ще поспати')
                self.current_state = self.sleeping
            if self.feel is True:
                print('Але добре я поспав!')
            if self.feel is False:
                print('A-a-a! Чорт забирай! Через цю тривогу\
 наче мішком прибитий...')
            if activity == '1':
                print('Йду вчитися.')
                self.current_state = self.studying
            elif activity == '2':
                print('Зранку завжди треба поснідати.')
                self.current_state = self.eating
            else:
                continue

fsm = StudentLifeFSM()
activities = input()
for activity in activities:
    fsm.send(activity)
