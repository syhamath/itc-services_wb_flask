# IT Consulting Services - Flask Web Application

## Overview

This is a Flask-based web application for an IT consulting company. The application provides a professional website with pages for services, partners, and contact information. It features a modern, responsive design using Bootstrap with a dark theme optimized for Replit.

## System Architecture

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Structure**: Modular design with separate route handling
- **Session Management**: Flask sessions with configurable secret key
- **Error Handling**: Custom 404 error pages
- **Logging**: Built-in Python logging for debugging and monitoring

### Frontend Architecture
- **Template Engine**: Jinja2 (Flask's default)
- **CSS Framework**: Bootstrap 5 with Replit dark theme
- **Icons**: Font Awesome for consistent iconography
- **Responsive Design**: Mobile-first approach with Bootstrap grid system
- **Theme**: Dark theme optimized for Replit environment

## Key Components

### Application Structure
- `app.py`: Main Flask application initialization
- `main.py`: Application entry point
- `routes.py`: URL routing and view functions
- `templates/`: Jinja2 HTML templates
- `static/`: CSS, images, and other static assets

### Core Pages
1. **Homepage** (`/`): Hero section with service overview
2. **Services** (`/services`): Detailed service offerings
3. **Partners** (`/partners`): Business partnership showcase
4. **Contact** (`/contact`): Contact form and business information

### Features
- Contact form with server-side validation
- Flash messaging system for user feedback
- Responsive navigation with active state indicators
- Professional card-based layouts
- SEO-friendly page titles and meta tags

## Data Flow

### Request Flow
1. User requests a URL
2. Flask routes the request to appropriate view function
3. View function processes any form data (if applicable)
4. Template is rendered with context data
5. Response is sent back to user

### Contact Form Processing
1. User submits contact form via POST
2. Server validates required fields
3. Form data is logged for record-keeping
4. Success/error flash message is displayed
5. User is redirected to prevent duplicate submissions

## External Dependencies

### CDN Resources
- Bootstrap 5 CSS (Replit dark theme variant)
- Font Awesome icons
- Bootstrap JavaScript (for responsive components)

### Python Dependencies
- Flask 2.3.2 (web framework)
- Standard library modules (os, logging)

## Deployment Strategy

### Development Environment
- Flask development server with debug mode
- Hot reloading for development
- Configurable host and port settings

### Production Considerations
- Environment-based secret key configuration
- Error handling for production deployment
- Static file serving optimization needed for production

### Replit Compatibility
- Designed for Replit environment
- Uses Replit-specific Bootstrap theme
- Configured for Replit's hosting requirements

## Changelog
- July 03, 2025. Initial setup

## User Preferences

Preferred communication style: Simple, everyday language.