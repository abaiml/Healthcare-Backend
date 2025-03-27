# Healthcare Backend API

This is a **Django REST Framework (DRF)** based backend for a healthcare management system.  
The API allows authenticated users to manage patients, doctors, and patient-doctor mappings securely.

## **Features**

- **Authentication** using JWT (JSON Web Tokens)
- **Patient Management** (CRUD operations)
- **Doctor Management** (CRUD operations)
- **Patient-Doctor Mapping** (Assigning doctors to patients)
- Secure API endpoints with **permissions and authentication**

## **Tech Stack**

- **Framework:** Django, Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Authentication:** JWT (`djangorestframework-simplejwt`)

## **Installation & Setup**

### **1. Clone the repository**
  ```
  git clone https://github.com/abaiml/PMS.git
  cd PMS
  ```

### **2. Create and Activate Virtual Environment**  
```
python -m venv djenv
source djenv/bin/activate  # On macOS/Linux
djenv\Scripts\activate  # On Windows
```

### **3. Install Dependencies**  
```
pip install -r requirements.txt
```

### **4. Set Up Environment Variables**  
Create a `.env` file in the project root and configure it based on `.env.example`.

### **5. Apply Migrations**  
```
python manage.py migrate
```

### **6. Run the Development Server**  
```
python manage.py runserver
```

## **API Endpoints**

### **Authentication**  
- `POST /api/auth/register/` - Register a new user  
- `POST /api/auth/login/` - Log in and receive JWT tokens  
- `POST /api/auth/token/refresh/` - Refresh access token  
- `POST /api/auth/logout/` - Log out and blacklist refresh token  

### **Patient Management**  
- `POST /api/patients/` - Create a patient  
- `GET /api/patients/` - List all patients  
- `GET /api/patients/<id>/` - Get patient details  
- `PUT /api/patients/<id>/` - Update patient details  
- `DELETE /api/patients/<id>/` - Delete a patient  

### **Doctor Management**  
- `POST /api/doctors/` - Create a doctor  
- `GET /api/doctors/` - List all doctors  
- `GET /api/doctors/<id>/` - Get doctor details  
- `PUT /api/doctors/<id>/` - Update doctor details  
- `DELETE /api/doctors/<id>/` - Delete a doctor  

### **Patient-Doctor Mapping**  
- `POST /api/mappings/` - Assign a doctor to a patient  
- `GET /api/mappings/` - List all patient-doctor mappings  
- `GET /api/mappings/<patient_id>/` - Get doctors assigned to a patient  
- `DELETE /api/mappings/delete/<id>/` - Remove doctor from patient  

## **Testing the API**

Use **Postman** or any API client to test the endpoints.  
Authentication requires sending a **JWT access token** in the `Authorization` header.

```
Authorization: Bearer <access_token>
```

## **Contact**

For any questions or clarifications, please reach out.  
