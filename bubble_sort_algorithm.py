lis=[20,60,51,33,17,66,44]
first_value=lis[0]
second_value=lis[1]
lenth_of_list=len(lis)-1
stage1=0
stage2=1

task_complete=False
while task_complete==False:
    if stage1>lenth_of_list:
            task_complete=True
    else:
        while lis[stage1]<lis[stage2]: #20 & 60 
            print(lis[stage1],lis[stage2])
            print("----------------------------")

            # swipe the values
            first_value=lis[stage1] #20
            second_value=lis[stage2] #60

            #swipe values inside of list
            lis[stage1]=second_value #60
            lis[stage2]=first_value #20
            print("new list : ",lis)

            #swipe the stage
            stage1=stage1+1 #2
            stage2=stage2+1 #3
            print("stage 1 ",stage1)
            print("stage 2 ",stage2,)
            print("----------------------------")
        else:
            stage1=stage1+1 #2
            stage2=stage2+1 #3
            print("stage 1 ",stage1)
            print("stage 2 ",stage2,)


        
