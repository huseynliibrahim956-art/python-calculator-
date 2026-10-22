import math
import numpy as np
import random as r
def functions():
    class funstions_part:
        def __init__(self,x,y):
            self.x=x
            self.y=y
    
    x_asked,y_asked=map(float,input('enter x and y each').split())
    user=funstions_part(x_asked,y_asked)
    print('x:',user.x)
    print('y:',user.y)
    print('--------------------------------')
    while True:
        print('1.find the distance between two')
        print('2.to find the perimeter of the rhombus that the center of it is (0,0)')
        print('3.to find the rectangle that the center of it is (0,0)')
        print('4.exit')
        def distance(x_asked,y_asked):
            d=math.sqrt(x_asked**2+y_asked**2)
            print(f'so the answer is {d:.2f}')
        def area_rhombus(x_asked,y_asked):
            z=math.sqrt(x_asked**2+y_asked**2)
            print(f'{z*4:.2f} is the answer')
        def rectangle_area(x_asked,y_asked):
            print(f'{4*x_asked*y_asked:.2f} is the answer')
        nums=int(input('enter a num'))
        match nums:
            case 1:
                distance(x_asked,y_asked)
            case 2:
                area_rhombus(x_asked,y_asked)
            case 3:
                rectangle_area(x_asked,y_asked)
            case 4:
                break
def geometry():
    while True:
        print('1.rectangle')
        print('2.circumtence,circle')
        print('3.triangle')
        print('4.exit')
        user=int(input('enter a num'))
        def rectangle():
            class  sides:
                def __init__(self,height,width):
                    self.height=height
                    self.width=width

            width_r,height_r=map(float,input('enter both sides:').split())
            rectangle1=sides(height_r,width_r)
            rectangle1.height=height_r
            rectangle1.width=width_r
            print('_______FORMULAS________')
            formulas_dict={
                '1.area':f'{width_r:.2f}*{height_r:.2f}',
                '2.perimeter':f'({width_r:.2f}+{height_r:.2f})*2'
            }
            for key,value in formulas_dict.items():
                print(f'{key}:{value}')
            asker=int(input('so we use this formulas to get the perimeter or area,enter the num')) 
            if asker==1:
                print(width_r*height_r)
                print('------------------')
            elif asker==2:
                print(int(width_r+height_r)*2)
            else:
                print('num not found.')
        def circumtence():
            v=input('enter the radius of the circle')
            if v.isdigit():
                v=float(v)
                print(f'{2*math.pi*v} is the perimeter and {math.pi*pow(v,2)} is the area of the circle')
            else:
                print(f'{v} not found')
        def triangle():
            class triangle_sides:
                def __init__(self,right,left,unders):
                    self.right=right
                    self.left=left
                    self.unders=unders
            class triangle1(triangle_sides):
                def __init__(self, right, left, unders,height):
                    super().__init__(right, left, unders)
                    self.height=height
                def asking():
                    right_t,left_t,unders_t,height_t=map(float,input('enter a the values of the sides by this queue (right,left underscore ,height)').split())
                    if right_t+left_t>unders_t and left_t+unders_t>right_t and right_t+unders_t>left_t:
                        return right_t,left_t,unders_t,height_t
                    else:
                        print('the sum of any 2 sides of the triangle must be bigger than the remaining 1')
            def main_part(right_t,left_t,unders_t,height_t):
                array=np.array([right_t,left_t,unders_t,height_t])
                triangle_help_dict={
                    'area':'1',
                    'perimeter':'2',
                    'median':'3',
                    'exit':'4'
                }
                for key,value in triangle_help_dict.items():
                    print(f'{key}:{value}')
                asker=int(input('enter the num:'))
                if asker==1:
                    xp=input('which height? lf left press l if right press r if unders press u ')
                    if xp=='l':
                        print(0.5*height_t*left_t)
                    elif xp=='r':
                        print(0.5*height_t*right_t)
                    elif xp=='u':
                        print(0.5*height_t*unders_t)
                    else:
                        print('we couldnt find')
                elif asker==2:
                    array=np.array([left_t,right_t,height_t,unders_t])
                    print(left_t+right_t+unders_t)
                elif asker==3:
                    print(round(0.5*math.sqrt(2*pow(left_t,2)+2*pow(right_t,2)-pow(unders_t,2),3)))
            values=triangle1.asking()
            if values is not None:
                main_part(*values)
        if user==1:
            rectangle()
        elif user==2:
            circumtence()
        elif user==3:
            triangle()
        elif user==4:
            break

def physics():
        while True:
            print('1.kinematics')
            print('2.circular motion')
            print('3.exit')
            user=input('enter a num.')
            if user.isdigit():
                user=int(user)
                def kinematic():
                    class kinematics:
                        def __init__(self,time,velocity,displacement):
                            self.time=time
                            self.velocity=velocity
                            self.displacement=displacement
                    class constant_velocity(kinematics):
                        pass
                    class changing_velocity(kinematics):
                        def __init__(self, time, velocity, displacement,acceleration):
                            super().__init__(time, velocity, displacement)
                            self.acceleration=acceleration
                    user=input('is your speed constant?press y if yes if not press n').lower()
                    if user=='y':
                        t,v,d=map(float,input('enter the nums by this queue time,velocity,displacement').split())
                        ques1=constant_velocity(time=t,velocity=v,displacement=d)
                        jp=input('enter which thing u wanna find out d t or v ?').lower()
                        match jp:
                            case 'd':
                                print(f'{ques1.velocity*ques1.time}')
                                print('-----------------------')
                            case 't':
                                print(f'{(ques1.displacement/ques1.velocity):.2f}')
                                print('------------------------')
                            case 'v':
                                print(f'{(ques1.displacement/ques1.time):.2f}')
                                print('-------------------------')
                        
                    elif user=='n':
                        t,v,d,a=map(float,input('enter the nums by this queue time,velocity,displacement and the acceleration').split())
                        ques2=changing_velocity(time=t,velocity=v,displacement=d,acceleration=a)
                        jh=input('enter which thing u wanna find out d t v or a?').lower()
                        match jh:
                            case 'a':
                                print(f'{2*ques2.displacement/pow(t,2):.2f}')
                                print('-----------------------')
                            case 'd':
                                print(f'{a*pow(t,2)/2}')
                                print('-----------------------')
                            case 't':
                                print(f'{math.sqrt(2*ques2.displacement/a):.2f}')
                                print('------------------------')
                            case 'v':
                                print(f'{math.sqrt(2*ques2.displacement*a):.2f}')
                                print('-------------------------')
                    else:
                        pass

                def circular():
                    class circular_motion:
                        def __init__(self,angular_velocity,angular_displacement,amount_of_cycles,time):
                            self.angular_velocity=angular_velocity
                            self.angular_displacement=angular_displacement        
                            self.amount_of_cycles=amount_of_cycles
                            self.time=time
                    class changin_velocity_circular(circular_motion):
                        def __init__(self, angular_velocity, angular_displacement, amount_of_cycles,time,acceleration):
                            super().__init__(angular_velocity, angular_displacement,time, amount_of_cycles)
                            self.acceleration=acceleration
                    class linear_velocity(changin_velocity_circular):
                        def __init__(self, angular_velocity, angular_displacement, amount_of_cycles, time, acceleration,linear_velocity):
                            super().__init__(angular_velocity, angular_displacement, amount_of_cycles, time, acceleration)
                            self.linear_velocity=linear_velocity
                    while True:
                        print('0.acceleration')
                        print('1.angular velocity')
                        print('3.angular displacement')
                        print('4.period')
                        print('5.frequency')
                        print('6.exit')
                        asker=input('enter the index of which equation do you wanna find out')
                        def accelerations():
                            in_case=input('do you wanna find it out with angular velocity or with the radius? press r if radius,press w if it is angular velocity').lower()
                            if in_case=='r':
                                v,r=map(float,input('enter the nums by this queue v(linear velocity),r(radius)').split())
                                ques1=linear_velocity(angular_velocity=0,angular_displacement=0,
                                                      amount_of_cycles=0,time=0,acceleration=v**2/r,linear_velocity=v)
                                print(f'{ques1.acceleration:.3f}')
                                print('---------------------------')
                            elif in_case=='w':
                                w,v=map(float,input('as you know there is no need to say but i ll say it js in case enter the nums by this queue w,v').split())
                                ques2=linear_velocity(angular_velocity=w,angular_displacement=0,amount_of_cycles=0,time=0,acceleration=w*v,linear_velocity=v)
                                print(f'{ques2.acceleration:.3f}')
                                print('--------------------------')
                            else:
                                print('couldnt find.')
                        def angular_velocity():
                            t,N=map(float,input('enter the nums by this queue t(time),N(number of cycles)').split())
                            ques1=circular_motion(angular_velocity=(2*math.pi*N)/t,angular_displacement=0,amount_of_cycles=N,time=t)
                            print(round(ques1.angular_velocity,3))
                            print('---------------------------------------------')

                        def angular_displacements():
                            def formulas():
                                class help:
                                    def __init__(self,time,cycles):
                                        self.cycles=cycles
                                        self.time=time
                                    @staticmethod
                                    def asking():
                                        time,cycles=map(float,input('enter the values by time,cycles').split())
                                        ques3=help(time,cycles)
                                        if time and cycles is not None:
                                         return time,cycles
                                x=help.asking()
                                return x
                            
                            def formula(time,cycles):
                                class formulass:
                                    def __init__(self,angular_d,period,frequency):
                                        self.angular_d=round(2*math.pi*cycles,3)
                                        self.period=round(time/cycles)
                                        self.frequency=round(cycles,time)
                                    @staticmethod
                                    def pri():
                                        print(round(2*math.pi*cycles,3))
                                        print('------------------------')
                                formulass.pri()
                                return formulass
                            
                            x=formulas()      
                            formula(*x)
                        def ft():
                            class Nt:
                                def __init__(self,N,t):
                                    self.N=N
                                    self.t=t
                                def asking():
                                    ti,Nu=map(float,input('enter the values of time and cycles').split())
                                    ques2=Nt(ti,Nu)
                                    return ti,Nu
                            
                            v=Nt.asking()
                            return v
                        z=ft()
                            
                        def period(ti,Nu):
                            class T:
                                def __init__(self,periods):
                                    self.periods=periods
                            ques4=T(periods=ti/Nu)
                            print(round(ques4.periods,3))
                        def frequency(ti,Nu):
                            class n:
                                def __init__(self,frequency):
                                    self.frequency=frequency
                            ques5=n(frequency=Nu/ti)
                            print(round(ques5.frequency,3))

                        if asker.isdigit():
                            asker=int(asker)
                            match asker:
                                case 0:
                                    accelerations()
                                case 1:
                                    angular_velocity()
                                case 3:
                                    angular_displacements()
                                case 4:
                                     if z is not None:
                                      period(*z)
                                case 5:
                                    if z is not None:
                                     frequency(*z)
                                case 6:
                                    break
                        else:
                            pass
                if user==1:
                    kinematic()
                elif user==2:
                    circular()
                elif user==3:
                    break
                else:
                    print('the num was expected to be between 1-3 included')
            else:
                print('you cant enter names sentences or words')
while True:
    print('1.functions')
    print('2.geometry')
    print('3.physics')
    first_question=input('enter a num')
    if first_question.isdigit():
        first_question=int(first_question)
        if first_question<5:
            match first_question:
                case 1:
                    functions()
                case 2:
                      geometry()
                case 3:
                    physics()
        else:
            pass
