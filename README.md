# QR Code Generator

A simple console-based QR Code Generator built using a procedural programming approach. I created this project to showcase my understanding of software design, code organisation, and building applications that are easy to maintain and scale over time.

Although the project is small, the structure is designed with future growth in mind. New features can be added without changing the application's core flow, making it a great foundation for larger projects.

---

## Why I Built This

After 5 years of programming experience, I've learned that writing code is only one part of software development. Creating applications that remain easy to understand, maintain, and extend is equally important.

This project demonstrates:

- Procedural programming concepts
- Separation of responsibilities
- Simple and clean code structure
- Configurable application settings
- Scalable menu and action management

---

## Features

The application provides four menu options:

### 1. Link / Text QR Generator

Generate QR codes from:

- Website URLs
- Plain text
- Notes
- Any custom string

### 2. Contact Card QR Generator

Generate QR codes containing contact information such as:

- Name
- Phone Number
- Email Address
- Organisation

This allows users to quickly save contact details by scanning the QR code.

### 3. WiFi QR Generator

Create QR codes for WiFi networks.

Users can scan the generated QR code and connect to the WiFi network without manually typing credentials.

### 4. Exit

Safely close the application.

---

## Project Design

### Procedural Approach

This application is intentionally built using a procedural programming style to demonstrate a strong understanding of programming fundamentals.

The logic is organised into focused functions that handle specific tasks, making the code:

- Easy to read
- Easy to debug
- Easy to maintain

---

## Customisation

The application uses a `settings.py` file to store initial configuration values.

This makes it simple to:

- Change default settings
- Update application behaviour
- Modify configuration without touching core logic

As the project grows, additional settings can be added without affecting existing functionality.

---

## Choice Manager

One of the key parts of the application is the **Choice Manager**.

The Choice Manager is responsible for:

- Handling user menu selections
- Routing actions to the correct feature
- Keeping the main application flow clean

Because of this design, adding new functionality is straightforward.

### Example

If you want to add a new QR generator type:

1. Create the new action/function.
2. Register it in the Choice Manager.
3. Add the menu option.

No major changes are required elsewhere in the application.

---

## Scalability

Even though this is a small console application, the structure was designed with future expansion in mind.

Possible future improvements include:

- Email QR codes
- SMS QR codes
- Social media profile QR codes
- Batch QR generation
- Logo embedding
- Export formats (PNG, SVG, PDF)
- Database integration
- GUI/Desktop version

The current architecture allows these features to be added with minimal changes to existing code.

---

## Project Goals

The purpose of this project is not only to generate QR codes but also to demonstrate:

- Clean procedural programming
- Maintainable code structure
- Configurable application design
- Forward-thinking architecture
- Software scalability principles

---

## Conclusion

This QR Code Generator is a small project with a simple purpose, but it reflects the way I approach software development: keeping things clean, understandable, and ready for future growth.

I believe good software is not just about making something work today, but making sure it can evolve tomorrow without becoming difficult to manage.
