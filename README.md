# E-Commerce_Django
MED-SHOP is e-commerce website is an online platform that allows individuals or businesses to buy and sell products and services over the internet.

Some of the key features of an e-commerce website :

### Product Catalogue:
A listing of all the products or services offered for sale on the website, with detailed descriptions, images, and prices.

### Shopping Cart:
A virtual cart that keeps track of all the items selected for purchase by the customer.

### Payment Gateway: 
A secure platform for processing customer payments, which can include credit card, debit card, or online payment services such as PayPal.

### Order Management:
A system that keeps track of customer orders, including order status, shipping information, and customer information.

### Customer Accounts:
A system that allows customers to create an account on the website, which can be used to store shipping information, payment information, and order history.

### Search and Filtering: 
A feature that allows customers to easily search for products and filter their results based on various criteria such as price, brand, and category.

### Responsive Design: 
A design that adjusts to different screen sizes and devices, ensuring a positive user experience on desktop, tablet, and mobile devices.

### Customer Service:
A system for providing support to customers, including live chat, email support, and a comprehensive FAQ section.

![](imgscrin/0.png)

## 1 Django Installation Structure Introduction

### database UML

![](imgscrin/1.png)

### Template implementation

Web Template of this prpoject: https://colorlib.com/wp/template/e-shop/
![](imgscrin/2.png)

## 2 Products

### database model admin relation category and product image upload

![](imgscrin/3.png)

### Implemet Richtext Editor Ckeditor

![](imgscrin/4.png)

### Product Image gallery

![](imgscrin/5.png)

### Variants de Product

![](imgscrin/6.png)

### Page Product detail with image gallery

![](imgscrin/7.png)

### Product Review Comment Rating

![](imgscrin/8.png)

## 3 Pages de contact

![](imgscrin/9.png)

## 4 Pages Search Products

![](imgscrin/10.png)

## 5 Pages login

![](imgscrin/11.png)

## 6 Pages sign Up

![](imgscrin/12.png)

## 7 Pages FAQ

## 8 Category Tree Subcategory menu('mptt')

![](imgscrin/13.png)

## 9 Shop cart Add list delete items

![](imgscrin/14.png)

### Order Prudacts and Detail

![](imgscrin/18.png)

## 10 user profile information

![](imgscrin/15.png)

### Update Change User & Profile Information

![](imgscrin/16.png)

### Change User Password

![](imgscrin/17.png)

## 11 Product Attributes Variants Amazon style Size Color

![](imgscrin/varaint.png)

Product Attributes Variants Amazon style Size Color (Database Model and Admin)

<ol>
    <li>Create Models</li>
        Color,
        Size,
        Variants
    <li>Add variant filed to Product</li>
        variant (Noe, Size-Color, Size, Color)
    <li>Install image thumbnails</li>
        pip install django-admin-thumbnails
        Define thumbnails variants images
    <li>Product Detail</li>
        Change product detail function  -views
        Change product link depending on variant --templates
        Add variants on product detail --templates
        Apply Ajax for getting Product variant --templates
        Add ajax function  -- View
        Select Variant Size, Color -templates
</ol>

![](imgscrin/6.png)
![](imgscrin/7.png)

## 12 Multi Language on Database Models and Multi Currency

This part Include Setting, Category, Product, FAQ, Userprofile Model and Admin, At the frontpages Product Detail, FAQ, Userprofile

![](imgscrin/Multi%20Language%20on%20Database.png)

![](imgscrin/19.png)

# Espace administrateur E-Commerce_Django

![](imgscrin/00.png)

#### Before running this project you need intall below list apps and packages

Install Python 3.7 or above -> https://www.python.org/

Install Pip -> python get-pip.py

pip install Django

pip install django-admin-thumbnails

pip install django-ckeditor

pip install django-currencies

pip install django-mptt

pip install Pillow

#### For running

python manage.py runserver
