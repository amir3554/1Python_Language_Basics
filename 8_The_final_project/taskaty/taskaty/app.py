from argparse import ArgumentParser #الوحدة اتي تتيح لنا بنا التطبيق سي ال اي على سطر الاوامر
#تحلل هذه الدالة الخيارات و الوسائط التي يمررها المستخدم الى التطبيق في سطر الاوامر
from .taskcontroller import TaskController
#argparse.ArgumentParser
#هذا الصنف يمثل محلل الوسائط الخاص بالتطبيق و هذا الصنف مسؤول عن تحويل النصوص المبكتوبة في سطر الوامر الى كائنات يمكن لبايثون التعال معها ويمتلك هذا الصنف عدد من التوابع التي تساعد في تعيين الوسائط الخاصة بالتطبيق و تحديد خصائصها

#parse_args()يعيد كائن  نام سبايس  من مدخلات المسخدم و الذي يشبه القواميس في بايثون حيث يكون المفتاح هو الوسيط و القيمة ان وجدت


#شرطة واحدة للخيار وعادة ما يليها الحرف الاول من اسم الخيار   و اعتماد شرطتين كصيغة مفصلة للخيار ويتلوها الاسم الكامل للخيار
#في البداية ننشئ نسخة من الصنف  ارغيومينت بارسر  ثم نضيف اليها الوسائط ثم نطلب من التابع  بارس ارغس  تحليلها و تحويلها الى الكائن  نام سبايس  الذي يمكن الاستفادة منه للحصول المدخلة من قبل المستخدم 
#default = none يسخدم هذا المعامل المفتاحي لتعيين قيمة الخيار الافتراضية في حال لم يدخلها المستخدم
#action يستخدم هذا المعامل المفتاحي لتعيين العملية التي يجب تنفيذها عند وجود هذا الخيار

def main():#سنكنب فيها الشيفرة الخاصة للعامل مع سطر الاوامر و الخيارات و الوسائط الممرة الى التطبيق و توجيهها الى التوابع المقابلة لها في الاصناف التي سيتم انشائها.
    controller = TaskController('Mytasks.txt')
    
    parser = ArgumentParser(description="Simple LCI task manager.")
    subparsers = parser.add_subparsers()#هذا هو محلل فرعي و يعيد نوع خاص من الكائنات يمتلك تابع واحد فقط و هو  ادد بارسر
    add_task = subparsers.add_parser('add', help="Add the given task. ")
    add_task.add_argument('title', help='The title of this task.', type=str)
    add_task.add_argument('-d', '--description', help='Short decription of the task',type=str, default=None)
    add_task.add_argument('-s', '--start_date', help='Date to begine the task.', type=str, default=None)
    add_task.add_argument('-e', '--end_date', help='Date to end the task.',type=str, default=None)
    add_task.add_argument('--done',help='Check whether the task is done or not.', default=False)
    add_task.set_defaults(func = controller.add_task)

    list_tasks = subparsers.add_parser('list', help='list unfinished tasks.')
    list_tasks.add_argument('-a', '--all', help='list all the tasks.', action='store_true')
    list_tasks.set_defaults(func = controller.Display)

    check_task = subparsers.add_parser('check', help='check the guven task.')
    check_task.add_argument('-t', '--task', help='Number of the task to be done, If not specified, last task will be removed.', type=int)
    check_task.set_defaults(func = controller.check_task)

    remove = subparsers.add_parser('remove', help='Remove a task.')
    remove.add_argument('-t', '--task', help='The task to be removed (number)', type=int)
    remove.set_defaults(func = controller.remove_task)

    reset = subparsers.add_parser('reset', help='Remove all tasks.')
    reset.set_defaults(func = controller.reset)


    args = parser.parse_args()#يؤدي هذان السطران الى تحويل التطبيق الى برنامج سطر الاوامر 
    args.func(args)


if __name__ == "__main__":
    main()





