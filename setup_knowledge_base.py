#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medical PDF Download Helper Script
This script provides guidance and examples for downloading medical PDFs
"""

import os
import sys
import io

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def print_header():
    print("=" * 70)
    print("  CareConnect Medical Chatbot - PDF Knowledge Base Setup")
    print("=" * 70)
    print()

def print_section(title):
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")

def check_data_directory():
    """Check if data directory exists"""
    data_dir = "data"
    if not os.path.exists(data_dir):
        print(f"❌ Error: '{data_dir}' directory not found!")
        print(f"   Creating '{data_dir}' directory...")
        os.makedirs(data_dir)
        print(f"✅ '{data_dir}' directory created successfully!")
    else:
        print(f"✅ '{data_dir}' directory exists")

    # Count PDF files
    pdf_files = [f for f in os.listdir(data_dir) if f.endswith('.pdf')]
    print(f"📄 Current PDF files in data/: {len(pdf_files)}")

    if pdf_files:
        print("\nFound PDF files:")
        for pdf in pdf_files:
            file_size = os.path.getsize(os.path.join(data_dir, pdf)) / (1024 * 1024)
            print(f"  - {pdf} ({file_size:.2f} MB)")
    else:
        print("⚠️  No PDF files found. Please add medical PDFs to continue.")

    return len(pdf_files)

def print_free_resources():
    """Print list of free medical resources"""
    print_section("📚 Free Medical Resources (Legal & Open Access)")

    resources = [
        {
            "name": "WHO (World Health Organization)",
            "url": "https://www.who.int/publications",
            "description": "Free health guidelines, reports, and educational materials"
        },
        {
            "name": "CDC (Centers for Disease Control)",
            "url": "https://www.cdc.gov/publications/",
            "description": "Disease prevention and health promotion resources"
        },
        {
            "name": "PubMed Central (PMC)",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/",
            "description": "Free full-text archive of biomedical literature"
        },
        {
            "name": "MedlinePlus",
            "url": "https://medlineplus.gov/",
            "description": "Health information from the National Library of Medicine"
        },
        {
            "name": "OpenMD",
            "url": "https://openmd.com/",
            "description": "Medical information and health resources"
        },
        {
            "name": "Medical Books Free",
            "url": "https://www.freemedicalbookspdf.net/",
            "description": "Collection of free medical textbooks (check licenses)"
        },
        {
            "name": "NCBI Bookshelf",
            "url": "https://www.ncbi.nlm.nih.gov/books/",
            "description": "Free biomedical books and documents"
        },
        {
            "name": "Open Textbook Library - Medicine",
            "url": "https://open.umn.edu/opentextbooks/subjects/medicine",
            "description": "Open-licensed medical textbooks"
        }
    ]

    for i, resource in enumerate(resources, 1):
        print(f"{i}. {resource['name']}")
        print(f"   URL: {resource['url']}")
        print(f"   Description: {resource['description']}")
        print()

def print_recommended_topics():
    """Print recommended medical topics to cover"""
    print_section("🎯 Recommended Medical Topics to Include")

    topics = [
        "General Medicine & Health",
        "Common Diseases (Diabetes, Hypertension, etc.)",
        "First Aid & Emergency Care",
        "Nutrition & Diet",
        "Mental Health & Wellness",
        "Preventive Care & Vaccinations",
        "Drug Information & Pharmacology",
        "Anatomy & Physiology",
        "Infectious Diseases",
        "Chronic Disease Management"
    ]

    for i, topic in enumerate(topics, 1):
        print(f"  {i:2d}. {topic}")
    print()

def print_download_instructions():
    """Print step-by-step download instructions"""
    print_section("📥 How to Download and Add PDFs")

    instructions = [
        "Visit one of the free resource websites listed above",
        "Search for medical topics relevant to your chatbot",
        "Download PDF files (ensure they are legally available)",
        "Save the PDF files to the 'data/' directory",
        "Verify the files are readable and not corrupted",
        "Run 'python ingest.py' to process the documents"
    ]

    for i, instruction in enumerate(instructions, 1):
        print(f"  Step {i}: {instruction}")
    print()

def print_example_search_queries():
    """Print example search queries"""
    print_section("🔍 Example Search Queries for Medical PDFs")

    queries = [
        "WHO disease prevention guidelines PDF",
        "CDC health education materials PDF",
        "free medical textbook PDF",
        "open access medical journal articles",
        "public health resources PDF",
        "medical treatment guidelines PDF",
        "drug information leaflet PDF",
        "first aid manual PDF free"
    ]

    print("Use these queries in search engines to find relevant PDFs:\n")
    for i, query in enumerate(queries, 1):
        print(f"  {i}. \"{query}\"")
    print()

def print_legal_notice():
    """Print legal and ethical considerations"""
    print_section("⚖️ Legal & Ethical Considerations")

    print("⚠️  IMPORTANT: Please ensure you:")
    print()
    print("  ✓ Only use documents you have the legal right to use")
    print("  ✓ Respect copyright and licensing terms")
    print("  ✓ Prefer open-access and public domain materials")
    print("  ✓ Do not include personal health information (PHI)")
    print("  ✓ Verify the accuracy and credibility of sources")
    print("  ✓ Comply with healthcare regulations (HIPAA, GDPR, etc.)")
    print()
    print("📌 This chatbot is for educational purposes only and should")
    print("   not replace professional medical advice.")
    print()

def print_next_steps(pdf_count):
    """Print next steps based on current state"""
    print_section("🚀 Next Steps")

    if pdf_count == 0:
        print("❌ No PDF files found in data/ directory")
        print()
        print("To continue:")
        print("  1. Download medical PDFs from the resources listed above")
        print("  2. Save them to the 'data/' directory")
        print("  3. Run this script again to verify")
        print("  4. Run 'python ingest.py' to create the vector database")
    else:
        print(f"✅ Found {pdf_count} PDF file(s) in data/ directory")
        print()
        print("Ready to proceed:")
        print("  1. Run 'python ingest.py' to create the vector database")
        print("  2. Wait for the processing to complete")
        print("  3. Run 'chainlit run chainlit_app.py' to start the chatbot")
        print("  4. Open http://localhost:8000 in your browser")
    print()

def main():
    """Main function"""
    print_header()

    # Check data directory and count PDFs
    pdf_count = check_data_directory()

    # Print all information
    print_free_resources()
    print_recommended_topics()
    print_download_instructions()
    print_example_search_queries()
    print_legal_notice()
    print_next_steps(pdf_count)

    print("=" * 70)
    print("  For more information, see README.md")
    print("=" * 70)
    print()

if __name__ == "__main__":
    main()
