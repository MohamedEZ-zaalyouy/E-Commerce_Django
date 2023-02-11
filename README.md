# E-Commerce_Django

## 1 Django Installation Structure Introduction

### database UML

![](imgscrin/1.png)

### Template implementation

Web Template of this prpoject: https://colorlib.com/wp/template/e-shop/
![](imgscrin/2.png)

### database model admin relation category and product image upload

## 2 Product Image gallery

## 3 Implemet Richtext Editor Ckeditor

## 4 Pages de contact

## 5 Pages Search Products

### Search Auto Products

## 6 Pages login

## 7 Pages sign Up

## 8 Pages FAQ

## 9 Page Product detail with image gallery

## 10 Product Review Comment Rating

## 11 Category Tree Subcategory menu('mptt')

## 12 Shop cart Add list delete items

## 13 user profile information

### Update Change User & Profile Information

### Change User Password

## 14 Order Prudacts and Detail

## 15 User Comments List and Delete

## 16 Count and Average of Products Reviews

## 17 Product Attributes Variants Amazon style Size Color

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
    <li> Set Admin for new models </li>
        Color,
        Size,
        Variants
    <li>Set Variants inline for Product in admin</li>
    <li>Product Detail</li>
        Change product detail function  -views
        Change product link depending on variant --templates
        Add variants on product detail --templates
        Apply Ajax for getting Product variant --templates
        Add ajax function  -- View
        Select Variant Size, Color -templates
    <li>Shopcart</li>
        Define  variant relation in shopcart -- Model
        Add variant id to shopcart --views
        Get variant price in list --templates
    <li>Order</li>
        Define variant relation in order  -- Model;
        Add variant_id to order table   -- views;
        Add variant in reduction from stock code -  views;
        Get variant information in order list list --templates;
    <li>User Orders product </li>
         Add variant image in order product list;
</ol>

## 18 Multi Language on static html files and Urls

## 19 Multi Language on Database Models

This part Include Setting, Category, Product, FAQ, Userprofile Model and Admin, At the frontpages Product Detail, FAQ, Userprofile

![](imgscrin/Multi%20Language%20on%20Database.png)

## 20 Multi Currency
