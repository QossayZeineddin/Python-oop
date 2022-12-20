import csv
import difflib
#read file student
from Student import *
from Presence import *
from PresenceReport import *
from StudentDuration import studentDuration
from chatReport import *

def readStudentLest(a):

    with open(a+"/ENCS3130-StudentList.csv" , newline='', encoding='cp1252') as f:

        fileCount = csv.reader(f)
        for row in fileCount:
            studentArray.append(student(row[0] , row[1]))


def ReadAttendanceFiles(b):

    with open(b+'/ENCS3130-02-25-2021-AR.csv' , newline='', encoding='cp1252') as f1:

        fileCount = csv.reader(f1)
        for row in fileCount:
            ENCS3130_02_25_2021_ARArray.append(presence(row[0] , row[1]))


    with open(b+'/ENCS3130-03-14-2021-AR.csv' , newline='', encoding='cp1252') as f2:

        fileCount = csv.reader(f2)
        for row in fileCount:
            ENCS3130_03_14_2021_ARArray.append(presence(row[0] , row[1]))


    with open(b+'/ENCS3130-03-25-2021-AR.csv' , newline='', encoding='cp1252') as f3:

        fileCount = csv.reader(f3)
        for row in fileCount:
            ENCS3130_03_25_2021_ARArray.append(presence(row[0] , row[1]))

    with open(b+'/ENCS3130-04-08-2021-AR.csv' , newline='', encoding='cp1252') as f4:

        fileCount = csv.reader(f4)
        for row in fileCount:
            ENCS3130_04_08_2021_ARArray.append(presence(row[0] , row[1]))

    with open(b+'/ENCS3130-04-22-2021-AR.csv' , newline='', encoding='cp1252') as f5:

        fileCount = csv.reader(f5)
        for row in fileCount:
            ENCS3130_04_22_2021_ARArray.append(presence(row[0] , row[1]))


    with open(b+'/ENCS3130-04-29-2021-AR.csv' , newline='', encoding='cp1252') as f6:

        fileCount = csv.reader(f6)
        for row in fileCount:
            ENCS3130_04_29_2021_ARArray.append(presence(row[0] , row[1]))


    # اخذ حضور و غياب الطلاب

    x=0
    for i in studentArray:
        duration.append(studentDuration(studentArray[x].id,studentArray[x].name , 0,0,0,0,0,0 ))
        x+=1


    duration[0].d1='Duration in meeeting ENCS3130-02-25-2021-PR'
    duration[0].d2='Duration in meeeting ENCS3130-03-14-2021-PR'
    duration[0].d3='Duration in meeeting ENCS3130-03-25-2021-PR'
    duration[0].d4='Duration in meeeting ENCS3130-04-8-2021-PR'
    duration[0].d5='Duration in meeeting ENCS3130-04-22-2021-PR'
    duration[0].d6='Duration in meeeting ENCS3130-04-29-2021-PR'


    attention = []
    x = 0
    for i in studentArray :
        vid = studentArray[x].id
        vname = studentArray[x].name
        var = ''.join(i for i in studentArray[x].name if not i.isdigit())
        x +=1

        xx = 0
        for ii in ENCS3130_02_25_2021_ARArray:
            var1 = ENCS3130_02_25_2021_ARArray[xx].name
            var1 = ''.join(i for i in var1 if not i.isdigit())
            var1 = ''.join(i for i in var1 if  i.isalnum())
            xx += 1

            #فحص نسبة التشابه بين قائمة الاسماء و طلاب الاسماء بالحصة
            y = difflib.SequenceMatcher(None ,var1 , var).ratio()
            if y > 0.4:
              attention.append(studentArray[x-1])

              for iv in duration:
                  if iv.id == studentArray[x-1].id:
                      iv.d1 = ENCS3130_02_25_2021_ARArray[xx -1].Duration



    repor = []
    for i in attention:
        if i not in repor:
              repor.append(i)



    for i in studentArray:
        report.append(resenceReport(i.id, i.name, 'a', 'a', 'a', 'a', 'a', 'a'))

    for i in report:
        for b in repor:
            if i.id == b.id:
                i.x1 = 'x'



    attention1 = []
    x = 0
    for i in studentArray :
        vid = studentArray[x].id
        vname = studentArray[x].name
        var = ''.join(i for i in studentArray[x].name if not i.isdigit())
        x +=1

        xx = 0
        for ii in ENCS3130_03_14_2021_ARArray:
            var1 = ENCS3130_03_14_2021_ARArray[xx].name
            var1 = ''.join(i for i in var1 if not i.isdigit())
            var1 = ''.join(i for i in var1 if  i.isalnum())
            xx += 1

            y = difflib.SequenceMatcher(None ,var1 , var).ratio()
            if y > 0.4:
              attention1.append(studentArray[x-1])
              for iv in duration:
                  if iv.id == studentArray[x-1].id:
                      iv.d2 = ENCS3130_03_14_2021_ARArray[xx-1].Duration

    repor1 = []
    for i in attention1:
        if i not in repor1:
              repor1.append(i)




    for i in report:
        for b in repor1:
            if i.id == b.id:
                i.x2 = 'x'





    attention2 = []
    x = 0
    for i in studentArray :
        vid = studentArray[x].id
        vname = studentArray[x].name
        var = ''.join(i for i in studentArray[x].name if not i.isdigit())
        x +=1
        xx = 0
        for ii in ENCS3130_03_25_2021_ARArray:
            var1 = ENCS3130_03_25_2021_ARArray[xx].name
            var1 = ''.join(i for i in var1 if not i.isdigit())
            var1 = ''.join(i for i in var1 if  i.isalnum())
            xx += 1
            y = difflib.SequenceMatcher(None ,var1 , var).ratio()
            if y > 0.4:
              attention2.append(studentArray[x-1])
              for iv in duration:
                  if iv.id == studentArray[x -1].id:
                      iv.d3 = ENCS3130_03_25_2021_ARArray[xx-1].Duration

    repor2 = []
    for i in attention2:
        if i not in repor2:
              repor2.append(i)

    for i in report:
        for b in repor2:
            if i.id == b.id:
                i.x3 = 'x'


    attention3 = []
    x = 0
    for i in studentArray :
        vid = studentArray[x].id
        vname = studentArray[x].name
        var = ''.join(i for i in studentArray[x].name if not i.isdigit())
        x +=1
        xx = 0
        for ii in ENCS3130_04_08_2021_ARArray:
            var1 = ENCS3130_04_08_2021_ARArray[xx].name
            var1 = ''.join(i for i in var1 if not i.isdigit())
            var1 = ''.join(i for i in var1 if  i.isalnum())
            xx += 1
            y = difflib.SequenceMatcher(None ,var1 , var).ratio()
            if y > 0.4:
              attention3.append(studentArray[x-1])
              for iv in duration:
                  if iv.id == studentArray[x-1].id:
                      iv.d4 = ENCS3130_04_08_2021_ARArray[xx-1].Duration

    repor3 = []
    for i in attention3:
        if i not in repor3:
              repor3.append(i)

    for i in report:
        for b in repor3:
            if i.id == b.id:
                i.x4 = 'x'



    attention4 = []
    x = 0
    for i in studentArray :
        vid = studentArray[x].id
        vname = studentArray[x].name
        var = ''.join(i for i in studentArray[x].name if not i.isdigit())
        x +=1
        xx = 0
        for ii in ENCS3130_04_22_2021_ARArray:
            var1 = ENCS3130_04_22_2021_ARArray[xx].name
            var1 = ''.join(i for i in var1 if not i.isdigit())
            var1 = ''.join(i for i in var1 if  i.isalnum())
            xx += 1
            y = difflib.SequenceMatcher(None ,var1 , var).ratio()
            if y > 0.4:
              attention4.append(studentArray[x-1])

              for iv in duration:
                  if iv.id == studentArray[x-1].id:
                      iv.d5 = ENCS3130_04_22_2021_ARArray[xx-1].Duration

    repor4 = []
    for i in attention4:
        if i not in repor4:
              repor4.append(i)

    for i in report:
        for b in repor4:
            if i.id == b.id:
                i.x5 = 'x'


    attention5 = []
    x = 0
    for i in studentArray :
        vid = studentArray[x].id
        vname = studentArray[x].name
        var = ''.join(i for i in studentArray[x].name if not i.isdigit())
        var = ''.join(i for i in var if i.isalnum())
        x +=1
        xx = 0
        for ii in ENCS3130_04_29_2021_ARArray:
            var1 = ENCS3130_04_29_2021_ARArray[xx].name
            var1 = ''.join(i for i in var1 if not i.isdigit())
            var1 = ''.join(i for i in var1 if  i.isalnum())
            xx += 1
            y = difflib.SequenceMatcher(None ,var1 , var).ratio()
            if y > 0.4:
              attention5.append(studentArray[x-1])

              for iv in duration:
                  if iv.id == studentArray[x-1].id:
                      iv.d6 = ENCS3130_04_29_2021_ARArray[xx-1].Duration


    repor5 = []
    for i in attention5:
        if i not in repor5:
              repor5.append(i)

    for i in report:
        for b in repor5:
            if i.id == b.id:
                i.x6 = 'x'



    report[0].x1='Attendance  in meeeting ENCS3130-02-25-2021-PR'
    report[0].x2='Attendance  in meeeting ENCS3130-03-14-2021-PR'
    report[0].x3='Attendance  in meeeting ENCS3130-03-25-2021-PR'
    report[0].x4='Attendance  in meeeting ENCS3130-04-8-2021-PR'
    report[0].x5='Attendance  in meeeting ENCS3130-04-22-2021-PR'
    report[0].x6='Attendance  in meeeting ENCS3130-04-29-2021-PR'









def ReadParticipationFiles(c):



    for i in studentArray:
        chatreport1.append(chatReport(i.id, i.name, 0, 0, 0, 0, 0, 0))




    chatName1 = []
    with open(c+'/ENCS3130-02-25-2021-PR.txt') as ft:
        for line in ft:
            chat1.append(line)

    cou = 0
    for rwoe in chat1:

        query = chat1[cou]

        stopwords = ['From', 'Everyone', "(Direct Message) ", 'to', '-', 'he']
        querywords = query.split()

        resultwords  = [word for word in querywords if word  not in stopwords]
        result = ' '.join(resultwords)
        result = ''.join(i for i in result if not i.isdigit())
        #result = ''.join(i for i in result if i.isalnum())
        result = result[2:]
        spl = result.split(':' , 1)
        result = spl[0]
        result = result.replace('Mohammad Jubran(Direct Message)' , ' ')
        result = ''.join(i for i in result if i.isalnum())

        chatName1.append(result.lower())
        cou += 1


    x = 0
    for i in chatreport1 :

        vname = chatreport1[x].name
        var = ''.join(i for i in chatreport1[x].name if not i.isdigit())
        var = var.lower()
        chatreport1[x ].y1 += 0
        x +=1

        xx = 0
        for ii in chatName1:
            var1 = chatName1[xx]

            xx += 1
            #فحص نسبة التشابه بين قائمة الاسماء و طلاب الاسماء بالحصة
            y = difflib.SequenceMatcher(None ,var1 , var).ratio()
            if y > 0.5:

                chatreport1[x-1].y1 += 1


    chatName2 = []
    with open(c + '/ENCS3130-03-14-2021-PR.txt') as ft:
        for line in ft:
            chat2.append(line)

    cou = 0
    for rwoe in chat2:
        query = chat2[cou]

        stopwords = ['From', 'Everyone', "(Direct Message) ", 'to', '-', 'he']
        querywords = query.split()

        resultwords = [word for word in querywords if word not in stopwords]
        result = ' '.join(resultwords)
        result = ''.join(i for i in result if not i.isdigit())
        # result = ''.join(i for i in result if i.isalnum())
        result = result[2:]
        spl = result.split(':', 1)
        result = spl[0]
        result = result.replace('Mohammad Jubran(Direct Message)', ' ')
        result = ''.join(i for i in result if i.isalnum())

        chatName2.append(result.lower())
        cou += 1

    x = 0
    for i in chatreport1:

        vname = chatreport1[x].name
        var = ''.join(i for i in chatreport1[x].name if not i.isdigit())
        var = var.lower()
        chatreport1[x].y1 += 0
        x += 1

        xx = 0
        for ii in chatName2:
            var1 = chatName2[xx]

            xx += 1
            # فحص نسبة التشابه بين قائمة الاسماء و طلاب الاسماء بالحصة
            y = difflib.SequenceMatcher(None, var1, var).ratio()
            if y > 0.5:
                chatreport1[x - 1].y2 += 1




    chatName3 = []
    with open(c+'/ENCS3130-03-25-2021-PR.txt') as ft:
        for line in ft:
            chat3.append(line)

    cou = 0
    for rwoe in chat3:
        query = chat3[cou]

        stopwords = ['From', 'Everyone', "(Direct Message) ", 'to', '-', 'he']
        querywords = query.split()

        resultwords = [word for word in querywords if word not in stopwords]
        result = ' '.join(resultwords)
        result = ''.join(i for i in result if not i.isdigit())
        # result = ''.join(i for i in result if i.isalnum())
        result = result[2:]
        spl = result.split(':', 1)
        result = spl[0]
        result = result.replace('Mohammad Jubran(Direct Message)', ' ')
        result = ''.join(i for i in result if i.isalnum())

        chatName3.append(result.lower())
        cou += 1

    x = 0
    for i in chatreport1:

        vname = chatreport1[x].name
        var = ''.join(i for i in chatreport1[x].name if not i.isdigit())
        var = var.lower()
        chatreport1[x].y1 += 0
        x += 1

        xx = 0
        for ii in chatName3:
            var1 = chatName3[xx]

            xx += 1
            # فحص نسبة التشابه بين قائمة الاسماء و طلاب الاسماء بالحصة
            y = difflib.SequenceMatcher(None, var1, var).ratio()
            if y > 0.5:
                chatreport1[x - 1].y3 += 1



    chatName4 = []
    with open(c+'/ENCS3130-04-08-2021-PR.txt') as ft:
        for line in ft:
            chat4.append(line)

    cou = 0
    for rwoe in chat4:
        query = chat4[cou]

        stopwords = ['From', 'Everyone', "(Direct Message) ", 'to', '-', 'he']
        querywords = query.split()

        resultwords = [word for word in querywords if word not in stopwords]
        result = ' '.join(resultwords)
        result = ''.join(i for i in result if not i.isdigit())
        # result = ''.join(i for i in result if i.isalnum())
        result = result[2:]
        spl = result.split(':', 1)
        result = spl[0]
        result = result.replace('Mohammad Jubran(Direct Message)', ' ')
        result = ''.join(i for i in result if i.isalnum())

        chatName4.append(result.lower())
        cou += 1

    x = 0
    for i in chatreport1:

        vname = chatreport1[x].name
        var = ''.join(i for i in chatreport1[x].name if not i.isdigit())
        var = var.lower()
        chatreport1[x].y1 += 0
        x += 1

        xx = 0
        for ii in chatName4:
            var1 = chatName4[xx]

            xx += 1
            # فحص نسبة التشابه بين قائمة الاسماء و طلاب الاسماء بالحصة
            y = difflib.SequenceMatcher(None, var1, var).ratio()
            if y > 0.5:
                chatreport1[x - 1].y4 += 1



    chatName5 = []
    with open(c+'/ENCS3130-04-22-2021-PR.txt') as ft:
        for line in ft:
            chat5.append(line)

    cou = 0
    for rwoe in chat5:
        query = chat5[cou]

        stopwords = ['From', 'Everyone', "(Direct Message) ", 'to', '-', 'he']
        querywords = query.split()

        resultwords = [word for word in querywords if word not in stopwords]
        result = ' '.join(resultwords)
        result = ''.join(i for i in result if not i.isdigit())
        # result = ''.join(i for i in result if i.isalnum())
        result = result[2:]
        spl = result.split(':', 1)
        result = spl[0]
        result = result.replace('Mohammad Jubran(Direct Message)', ' ')
        result = ''.join(i for i in result if i.isalnum())

        chatName5.append(result.lower())
        cou += 1

    x = 0
    for i in chatreport1:

        vname = chatreport1[x].name
        var = ''.join(i for i in chatreport1[x].name if not i.isdigit())
        var = var.lower()
        chatreport1[x].y1 += 0
        x += 1

        xx = 0
        for ii in chatName5:
            var1 = chatName5[xx]

            xx += 1
            # فحص نسبة التشابه بين قائمة الاسماء و طلاب الاسماء بالحصة
            y = difflib.SequenceMatcher(None, var1, var).ratio()
            if y > 0.5:
                chatreport1[x - 1].y5 += 1


    chatName6 = []
    with open(c+'/ENCS3130-04-29-2021-PR.txt') as ft:
        for line in ft:
            chat6.append(line)

    cou = 0
    for rwoe in chat6:
        query = chat6[cou]

        stopwords = ['From', 'Everyone', "(Direct Message) ", 'to', '-', 'he']
        querywords = query.split()

        resultwords = [word for word in querywords if word not in stopwords]
        result = ' '.join(resultwords)
        result = ''.join(i for i in result if not i.isdigit())
        # result = ''.join(i for i in result if i.isalnum())
        result = result[2:]
        spl = result.split(':', 1)
        result = spl[0]
        result = result.replace('Mohammad Jubran(Direct Message)', ' ')
        result = ''.join(i for i in result if i.isalnum())

        chatName6.append(result.lower())
        cou += 1

    x = 0
    for i in chatreport1:

        vname = chatreport1[x].name
        var = ''.join(i for i in chatreport1[x].name if not i.isdigit())
        var = var.lower()
        chatreport1[x].y1 += 0
        x += 1

        xx = 0
        for ii in chatName6:
            var1 = chatName6[xx]

            xx += 1
            # فحص نسبة التشابه بين قائمة الاسماء و طلاب الاسماء بالحصة
            y = difflib.SequenceMatcher(None, var1, var).ratio()
            if y > 0.5:
                chatreport1[x - 1].y6 += 1


    chatreport1[0].y1='number of maseege in meeeting ENCS3130-02-25-2021-PR'
    chatreport1[0].y2='number of maseege in meeeting ENCS3130-03-14-2021-PR'
    chatreport1[0].y3='number of maseege in meeeting ENCS3130-03-25-2021-PR'
    chatreport1[0].y4='number of maseege in meeeting ENCS3130-04-8-2021-PR'
    chatreport1[0].y5='number of maseege in meeeting ENCS3130-04-22-2021-PR'
    chatreport1[0].y6='number of maseege in meeeting ENCS3130-04-29-2021-PR'


#for rr in chatreport1:
#    print(rr.id , rr.name  , rr.y1 , rr.y2 , rr.y3 , rr.y4  , rr.y5 ,  rr.y6  )



def writeCaht(d):
    #try:
        filename = d + '/ZoomChatReport.csv'
        with open(filename, 'w') as f:
            writer = csv.writer(f)


            for item in chatreport1 :
                writer.writerow([item.id, item.name, item.y1 ,item.y2 ,item.y3 ,item.y4 ,item.y5 , item.y6])

    #except BaseException as e:
     #   print('BaseException:', filename)



def writeDuration(d):
       # try:
            filenames = d + '/ClassDurationReport.csv'
            with open(filenames, 'w') as fs:
                writer = csv.writer(fs)
                for items in duration :
                    writer.writerow([items.id , items.name , items.d1 , items.d2, items.d3, items.d4, items.d5,items.d6])

       # except BaseException as e:
         #       print('BaseException:', filenames)



def writeAttendancs(d):
    #try:
            filename = d + '/ClassAttendanceReport.csv'
            with open(filename, 'w') as f:
                 writer = csv.writer(f)
                 x=0
                 for item in report :
                    writer.writerow([report[x].id, report[x].name, report[x].x1 , report[x].x2 ,report[x].x3 ,report[x].x4 ,report[x].x5 , report[x].x6])
                    x=x+1
    #except BaseException as e:
           # print('BaseException:', filename)




def dropEntriesAtTheEnd(minBe , c):



   mint = chat1[len(chat1)-1].split(':')
   check = int(mint[1]) - int(minBe)
   file1  = open(c+'/NewENCS3130-02-25-2021-PR-DropEnd.txt', 'w')
   for i1 in chat1:
        v = i1.split(' ' )
        v2 = v[0] .split(':')
        if v2[0].isnumeric() and int (v2[0]) < int(mint[0]):
            file1.write(i1)
        elif v2[0].isnumeric() and int (v2[0]) == int(mint[0]) and int(v2[1]) < check :
                    file1.write(i1)


   mint = chat2[len(chat2)-1].split(':')
   check = int(mint[1]) - int(minBe)
   file2  = open(c+'/NewENCS3130-03-14-2021-PR-DropEnd.txt', 'w')
   for i1 in chat2:
        v = i1.split(' ' )
        v2 = v[0] .split(':')
        if v2[0].isnumeric() and int (v2[0]) < int(mint[0]):
            file2.write(i1)
        elif v2[0].isnumeric() and int (v2[0]) == int(mint[0]) and int(v2[1]) < check :
                    file2.write(i1)


   mint = chat3[len(chat3)-1].split(':')
   check = int(mint[1]) - int(minBe)
   file3  = open(c+'/NewENCS3130-03-25-2021-PR-DropEnd.txt', 'w')
   for i1 in chat3:
        v = i1.split(' ' )
        v2 = v[0] .split(':')
        if v2[0].isnumeric() and int (v2[0]) < int(mint[0]):
            file3.write(i1)
        elif v2[0].isnumeric() and int (v2[0]) == int(mint[0]) and int(v2[1]) < check :
                    file3.write(i1)



   mint = chat4[len(chat4)-1].split(':')
   check = int(mint[1]) - int(minBe)
   file4  = open(c+'/NewENCS3130-04-08-2021-PR-DropEnd.txt', 'w')
   for i1 in chat4:
        v = i1.split(' ' )
        v2 = v[0] .split(':')
        if v2[0].isnumeric() and int (v2[0]) < int(mint[0]):
            file4.write(i1)
        elif v2[0].isnumeric() and int (v2[0]) == int(mint[0]) and int(v2[1]) < check :
                     file4.write(i1)

   mint = chat5[len(chat5)-1].split(':')
   check = int(mint[1]) - int(minBe)
   file5  = open(c+'/NewENCS3130-04-22-2021-PR-DropEnd.txt', 'w')
   for i1 in chat4:
        v = i1.split(' ' )
        v2 = v[0] .split(':')
        if v2[0].isnumeric() and int (v2[0]) < int(mint[0]):
            file5.write(i1)
        elif v2[0].isnumeric() and int (v2[0]) == int(mint[0]) and int(v2[1]) < check :
                     file5.write(i1)


   mint = chat6[len(chat6)-1].split(':')
   check = int(mint[1]) - int(minBe)
   file6  = open(c+'/NewENCS3130-04-29-2021-PR-DropEnd.txt', 'w')
   for i1 in chat4:
        v = i1.split(' ' )
        v2 = v[0] .split(':')
        if v2[0].isnumeric() and int (v2[0]) < int(mint[0]):
                file6.write(i1)
        elif v2[0].isnumeric() and int (v2[0]) == int(mint[0]) and int(v2[1]) < check :
               file6.write(i1)


def dropEntriesAtTheBeginning(minBe, c):
    mint = chat1[0].split(':')
    check = int(mint[1]) + int(minBe)
    file1 = open(c + '/NewENCS3130-02-25-2021-PR.txt', 'w')
    for i1 in chat1:
        v = i1.split(' ')
        v2 = v[0].split(':')
        if v2[0].isnumeric() and int(v2[0]) > int(mint[0]):
             file1.write(i1)
        elif v2[0].isnumeric() and int(v2[0]) == int(mint[0]) and int(v2[1]) > check:
             file1.write(i1)




    mint = chat2[0].split(':')
    check = int(mint[1]) + int(minBe)
    file2 = open(c + '/NewENCS3130-03-14-2021-PR.txt', 'w')
    for i1 in chat2:
        v = i1.split(' ')
        v2 = v[0].split(':')
        if v2[0].isnumeric() and int(v2[0]) > int(mint[0]):
            file2.write(i1)
        elif v2[0].isnumeric() and int(v2[0]) == int(mint[0]) and int(v2[1]) > check:
            file2.write(i1)

    mint = chat3[0].split(':')
    check = int(mint[1]) + int(minBe)
    file3 = open(c + '/NewENCS3130-03-25-2021-PR.txt', 'w')
    for i1 in chat3:
        v = i1.split(' ')
        v2 = v[0].split(':')
        if v2[0].isnumeric() and int(v2[0]) > int(mint[0]):
            file3.write(i1)
        elif v2[0].isnumeric() and int(v2[0]) == int(mint[0]) and int(v2[1]) > check:
            file3.write(i1)

    mint = chat4[0].split(':')
    check = int(mint[1]) + int(minBe)
    file4 = open(c + '/NewENCS3130-04-08-2021-PR.txt', 'w')
    for i1 in chat4:
        v = i1.split(' ')
        v2 = v[0].split(':')
        if v2[0].isnumeric() and int(v2[0]) > int(mint[0]):
            file4.write(i1)
        elif v2[0].isnumeric() and int(v2[0]) == int(mint[0]) and int(v2[1]) > check:
            file4.write(i1)

    mint = chat5[0].split(':')
    check = int(mint[1]) + int(minBe)
    file5 = open(c + '/NewENCS3130-04-22-2021-PR.txt', 'w')
    for i1 in chat5:
        v = i1.split(' ')
        v2 = v[0].split(':')
        if v2[0].isnumeric() and int(v2[0]) > int(mint[0]):
            file5.write(i1)
        elif v2[0].isnumeric() and int(v2[0]) == int(mint[0]) and int(v2[1]) > check:
            file5.write(i1)

    mint = chat6[0].split(':')
    check = int(mint[1]) + int(minBe)
    file6 = open(c + '/NewENCS3130-04-29-2021-PR.txt', 'w')
    for i1 in chat6:
        v = i1.split(' ')
        v2 = v[0].split(':')
        if v2[0].isnumeric() and int(v2[0]) > int(mint[0]):
            file6.write(i1)
        elif v2[0].isnumeric() and int(v2[0]) == int(mint[0]) and int(v2[1]) > check:
            file6.write(i1)

    print("Doneeeeeeeeeeeeeee")


def attendedmore(num ,d):

    nweAttendancs = []

    for at in report:
        nweAttendancs.append(at)

    for stu in duration:
        print(type(stu.d1) ,  type(num))
        print(stu.d1, num)
        if str(stu.d1) <= num :
            for rt in nweAttendancs:
                if rt.id == stu.id:
                    rt.x1 ='a'
        if str(stu.d2) <= num :
            for rt in nweAttendancs:
                if rt.id == stu.id:
                    rt.x2 ='a'
        if str(stu.d3) <= num :
            for rt in nweAttendancs:
                if rt.id == stu.id:
                    rt.x3 ='a'

        if str(stu.d4) <= num :
            for rt in nweAttendancs:
                if rt.id == stu.id:
                    rt.x4 ='a'
        if str(stu.d5) <= num :
            for rt in nweAttendancs:
                if rt.id == stu.id:
                    rt.x5 ='a'
        if str(stu.d6) <= num :
            for rt in nweAttendancs:
                if rt.id == stu.id:
                    rt.x6 ='a'

   # try:
        filename = d + '/NewAttendanceReport.csv'
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            x = 0
            for item in nweAttendancs:
                writer.writerow(
                    [item.id, item.name, item.x1, item.x2, item.x3, item.x4, item.x5,item.x6])
                x = x + 1
    #except BaseException as e:
     #   print('BaseException:', filename)

#for j in duration:
#    print(j.id , j.name , j.d1 , j.d2 , j.d3 , j.d4 ,j.d5 , j.d6)




studentArray = []
chatreport1 = []
report = []
duration =[]
ENCS3130_02_25_2021_ARArray = []
ENCS3130_03_14_2021_ARArray = []
ENCS3130_03_25_2021_ARArray = []
ENCS3130_04_08_2021_ARArray = []
ENCS3130_04_22_2021_ARArray = []
ENCS3130_04_29_2021_ARArray = []
chat1= []
chat2 = []
chat3 = []
chat4 = []
chat5 = []
chat6 = []


# read csv file
a =input("A, Please Eter the Path to Student List Sheet:")
#a="/home/qossay/PycharmProjects/LunixProject"
readStudentLest(a)
b= input("B, Please Enter the Path to the folder of Meeting Attendance Reports: ")
#b="/home/qossay/PycharmProjects/LunixProject/AttendanceFiles"
ReadAttendanceFiles(b)

c= input("c, Please Enter the Path to the folder of Meeting Participation Reports: ")
#c="/home/qossay/PycharmProjects/LunixProject/ParticipationFiles"
ReadParticipationFiles(c)
d= input("d, Please Enter the Path to store all output documents/folders: ")
#d="/home/qossay/PycharmProjects/LunixProject/outputFiles"
writeCaht(d)
writeDuration(d)
writeAttendancs(d)


while(True):
    print("\nEnter p for: consider students who attended more that P minutes in the meeting. ")
    print("Enter tp for: drop some entries at the beginning of all Meeting Participation Reports. ")
    print("Enter te for: drop some entries at the End of all Meeting Participation Reports.")
    print("Enter 'x' to exit the programme.\n")
    chis = input("youer chiose is: ")
    if chis.lower() == 'p':

        number = input("enter the num")
        attendedmore(number,d)
        print("\nA new report of attendance was create as name'NewAttendanceReport'\n ")

    if chis.lower() =='tp':
        v=input("Enter how many minute: ")
        dropEntriesAtTheBeginning(v,c)
        print("\ndrop the maseege in zoom meeting that send in the first", v, "minutes was successfully")

    if chis.lower() =='te':
        v=input("Enter how many minute: ")
        dropEntriesAtTheEnd(v,c)
        print("\ndrop the maseege in zoom meeting that send in the last",v,"minutes was successfully")

    if chis.lower() == 'x':
        exit(1)
