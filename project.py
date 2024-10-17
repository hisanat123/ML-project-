import streamlit as st
import pickle
from PIL import Image

def main():
    st.title(":rainbow[Predict student's dropout and academic success]")
    image = Image.open('predicting-student-dropout-using-machine-learning.jpg')
    st.image(image,width=800)


    Marital_status = st.selectbox(":green[Marital status]",[1,2,3,4,5,6])

    Application_mode = st.selectbox(":green[Application mode]",[1,17,39,43,44,7,18,42,51,16,53,15,5,10,2,57,26,27])

    Application_order = st.selectbox(":green[Application order]",[1,2,3,4,5,6,78,9,0])
    
    Course = st.selectbox(":green[Course]",[9500,9147,9238,9085,9773,9670,9991,9254,9070,171,8014,9003,9853,9119,9130,9556,33])
    
    Daytime_evening_attendance_t = st.selectbox(":green[Daytime/evening attendance]",[1,0])
    
    Previous_qualification = st.selectbox(":green[Previous qualification]",[1,2,3,4,5,6,9,39,19,12,40,42,38,43,10,15,14])
    
    Previous_qualification_grade = st.selectbox(":green[Previous qualification (grade)]",[133.0,130.0,140.0,120.0,150.0,133.0,175.0,117.0,188.0,126.0])
    
    Mothers_occupation = st.selectbox(":green[Mother's occupation ]",[19,1,37,38,3,4,42,2,34,12,40,9,5,39,11,41,30,14,35,36,6,10,29,43,18,22,27,26,44])
    
    Fathers_occupation = st.selectbox(":green[Father's occupation ]",[12,3,37,38,1,19,5,4,34,2,39,11,9,36,26,40,14,20,35,41,22,13,29,43,18,42,10,6,30,25,44,33,27,31])

    Admission_grade = st.selectbox(":green[Admission grade]",[130.0,140.0,120.0,100.0,150.0,150.6,184.4,102.0,147.0,156])
   
    Displaced = st.selectbox(":green[Displaced]",[1,0])
   
    Debtor = st.selectbox(":green[Debtor]",[1,0])
    
    Tuition_fees_up_to_date = st.selectbox(":green[Tuition fees up to date]",[1,0])
    
    Gender = st.selectbox(":green[Gender]",[1,0])

    Scholarship_holder = st.selectbox(":green[Scholarship holder]",[1,0])
    
    Age = st.text_input(":green[Age]","type_here")

    Curricular_units_1st_sem_credited = st.selectbox(":green[Curricular units 1st sem (credited)]",[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
   
    Curricular_units_1st_sem_enrolled = st.selectbox(":green[Curricular units 1st sem (enrolled)]",[0 ,6 ,5,7,8,1,12,10,18,9,21,3,17,16,11,14,13,2,4,15,19,23,26])
   
    Curricular_units_1st_sem_evaluations = st.selectbox(":green[Curricular units 1st sem (evaluations)]",
                                                        [ 0,6,8,9,10,5,7,14,12,15,13,11,1,17,18,19,21,4,16,3,24,2,22,45,
                                                         20,26,29,36,32,23,27,31,28,25,33])
    Curricular_units_1st_sem_approved = st.selectbox(":green[Curricular units 1st sem (approved)]",[ 0,6,5,7,4,1,3,2,8,18,10,9,21,11,13,12,16,14,17,19,15,20,26])
   
    Curricular_units_1st_sem_grade = st.selectbox(":green[Curricular units 1st sem (grade)]",[0,14,13.42857143,12.33333333, 11.85714286, 13.3,
                                                                                              13.875,11.4,13.21428571 ,10.57142857 ,13.25,13.2,
                                                                                              12,13.30625,12.5, 11.66666667, 11.4375,12.85714286,
                                                                                              13.375,13.29666667, 11.6,11.375,12.66666667, 12.93333333,
                                                                                              12.83333333, 11.33333333, 12.4, 10,11 , 12.7,11.9 ,12.57142857 ,11.2 ,11.975 ,10.33333333, 
                                                                                              14.84285714 ,12.2,12.16666667, 13.08,10.66666667 ,11.875,
                                                                                              13.85714286, 13.4,12.51666667, 11.61666667 ,13.14285714, 12.6])

    
    Curricular_units_2st_sem_credited = st.selectbox(":green[Curricular units 2st sem (credited)]",[ 0 ,1,2,5,7,4,10,3 ,13,9 ,6,11,12,8,14,15,16,18,19])
  
    Curricular_units_2st_sem_enrolled = st.selectbox(":green[Curricular units 2st sem (enrolled)]",[ 0,6,5,7,8,1,12,10,18,9,21,3,17,16,11,14,13,2,4,15,19,23,26])
   
    Curricular_units_2st_sem_evaluations = st.selectbox(":green[Curricular units 2st sem (evaluations)]",[ 0, 6,5,8,7,11,12,9,13,19,3,10,4,17,2,1,14,15,16,23,18,21])
   
    Curricular_units_2st_sem_approved = st.selectbox(":green[Curricular units 2st sem (approved)]",[ 0,6,5,8,2,7,4,1,3,10,13,11,19,9,12,17,14,20,16,18])
   
    Curricular_units_2st_sem_grade = st.selectbox(":green[Curricular units 2st sem (grade)]",[0.0,14.0,13.42857143,12.33333333,11.85714286,13.3,13.875,11.4,
                                                                                                    13.21428571,10.57142857,13.25,13.212,13.30625,15.95714286, 12.625,13.49666667,
                                                                                                    11.77777778,12.42857143, 12.5075,12.09090909, 14.6,13.82857143, 12.5375,12.1625,
                                                                                                    12.45,11.45454545])
   
   

    Curricular_units_2nd_sem_without_evaluations = st.selectbox(":green[Curricular units 2st sem (grade)]",[0,5,2,1,3,6,4,12,7,8])

    GDP = st.selectbox(":green[GDP]",[ 1.74,0.79,-3.12,-0.92,-4.06,3.51,-1.7,2.02,0.32,1.79])


  
       
      
   

    
    

    features = [ Marital_status,Application_mode,Application_order,Course,Daytime_evening_attendance_t,Previous_qualification,Previous_qualification_grade,
                 Mothers_occupation,Fathers_occupation,Admission_grade,Displaced,Debtor,Tuition_fees_up_to_date,Gender,Scholarship_holder,Age,Curricular_units_1st_sem_credited,
                Curricular_units_1st_sem_enrolled,Curricular_units_1st_sem_evaluations,Curricular_units_1st_sem_approved,
                Curricular_units_1st_sem_grade,Curricular_units_2st_sem_credited,Curricular_units_2st_sem_enrolled,Curricular_units_2st_sem_evaluations,
                Curricular_units_2st_sem_approved,Curricular_units_2st_sem_grade,Curricular_units_2nd_sem_without_evaluations,GDP
                ]

    model = pickle.load(open('model.sav','rb'))
    scalar = pickle.load(open('scaler.sav','rb'))

    pred = st.button('PREDICT')

    if pred:
        prediction = model.predict(scalar.transform([features]))

        if prediction == 0:
            st.write("Student is Dropout")
        elif prediction == 1:
            st.write("Student is Enrolled")
        else:
            st.write("Student is Graduated")

    


main()
    
