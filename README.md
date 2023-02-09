# E-Commerce_Django

## 1 -Django Installation Structure Introduction

## 2 -Django E-Commerce: css web template implementation

## 3 -Django E-Commerce: database model admin relation category and product image upload

## 5 -Django E-Commerce: Product Image gallery

## 6 -Django E-Commerce: Implemet Richtext Editor Ckeditor

## 7 -Django E-Commerce: Pages de contact

## 8 -Django E-Commerce: Category Tree Subcategory menu('mptt')

## 10 -Django E Commerce Automatically Creating Slug for Category and Product

## 11 -Django E Commerce Dynamic Slider in homepage

## 12 -Django E Commerce products with images on homepage

## 13 -Django E Commerce Listing Category products

## 14 -Django E Commerce Search Products

## 15 -Django E Commerce Search Auto Products

## 16 -Django E Commerce Product detail page with image gallery

## 17 -Django E Commerce Product Review Comment Rating

## 18 -Django E Commerce Shop cart Add list delete items

## 19 -Django E Commerce user profile information

## 20 -Django E Commerce user custom login logout user image

## 21 -Django E Commerce user custom sign Up user

## 22 -Django E Commerce Order Prudacts

## 23 -Django E Commerce User Menu & Panel Profile Page

## 24 -Django E Commerce Update Change User & Profile Information

## 25 -Django E Commerce Change User Password

## 26 -Django E Commerce User Order Product List and Detail

## 27 -Django E Commerce User Comments List and Delete

## 28 -Django E Commerce Count and Average of Products Reviews

## 29 -Django E Commerce Frequently Asked Questions FAQ with Jquery ui Accordion

## 30 -Django E Commerce Product Attributes Variants Amazon style Size Color

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

## 32 Access to functions from templates Tags

## 33 Multi Language on static html files and Urls
