# Django Amazon Backend 

## **Features installed**

- Amazon Bucket S3 Installed to store, with Django-storage + Django CleanUp
- Undertand Nested Objects in Serializer 
    * List Serializer not used because to Array Iteration 
    * Only Nested with put Method without List



## **Knowledge**
- Instance is from QuerySet in View 
- Validated_data is from request.data received from API, and going through serializer after data validation.
- Method Update, Create, Delete .. 
- @permission_classes([]) to disable authentication via Authentication
- Creation of special API Folder to Route API only with URLs.
- Views are implemented by method Switch
    * if request.method == 'GET' 
    * if request.method == 'PUT' 
 

## **Todo LIST**
- Custom JWT 
- check OAuth V2

#### **Librairies Installed** 

- Django==4.0.5
    *  asgiref==3.5.2
    *  backports.zoneinfo==0.2.1
    *  boto3==1.24.19
    *  botocore==1.27.19
    *  python-dateutil==2.8.2
    *  pytz==2022.1
    *  s3transfer==0.6.0
    *  six==1.16.0
    *  sqlparse==0.4.2
    *  tzdata==2022.1
    *  urllib3==1.26.9

- Other Libraries
  * django-cleanup==6.0.0
  * Pillow==9.1.1 
  * django-cors-headers==3.13.0
  * django-filter==22.1
  * django-phone-field==1.8.1
  * djangorestframework==3.13.1
  * djangorestframework-simplejwt==5.2.0
  * PyJWT==2.4.0
  * jmespath==1.0.1
  * Bucket Amazon Connection
     * django-storages==1.12.3








