#!/usr/bin/env python3
"""
SARIF Pie Chart Visualizer
Creates various pie chart visualizations from SARIF file data
"""

import json
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import numpy as np

def load_sarif_file(filepath):
    """Load and parse the SARIF file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading SARIF file: {e}")
        return None

def extract_sarif_data(sarif_data):
    """Extract relevant data from SARIF structure"""
    if not sarif_data or 'runs' not in sarif_data:
        return None
    
    results = []
    rules_info = {}
    
    for run in sarif_data['runs']:
        # Extract rules information
        if 'tool' in run and 'driver' in run['tool'] and 'rules' in run['tool']['driver']:
            for rule in run['tool']['driver']['rules']:
                rules_info[rule['id']] = {
                    'name': rule.get('name', rule['id']),
                    'description': rule.get('shortDescription', {}).get('text', ''),
                    'severity': rule.get('defaultConfiguration', {}).get('level', 'unknown'),
                    'security_severity': rule.get('properties', {}).get('security-severity', 0),
                    'tags': rule.get('properties', {}).get('tags', [])
                }
        
        # Extract results
        if 'results' in run:
            for result in run['results']:
                rule_id = result.get('ruleId', 'unknown')
                rule_info = rules_info.get(rule_id, {})
                
                result_data = {
                    'rule_id': rule_id,
                    'rule_name': rule_info.get('name', rule_id),
                    'severity': result.get('level', rule_info.get('severity', 'unknown')),
                    'security_severity': float(rule_info.get('security_severity', 0)),
                    'message': result.get('message', {}).get('text', ''),
                    'tags': rule_info.get('tags', []),
                    'locations': len(result.get('locations', [])),
                    'cwe_tags': [tag for tag in rule_info.get('tags', []) if tag.startswith('external/cwe/')]
                }
                results.append(result_data)
    
    return results, rules_info

def create_severity_pie_chart(results):
    """Create pie chart showing severity distribution"""
    severity_counts = Counter([r['severity'] for r in results])
    
    if not severity_counts:
        return
    
    # Define colors for different severity levels
    colors = {
        'error': '#ff4444',
        'warning': '#ff8800', 
        'note': '#ffcc00',
        'info': '#44ff44',
        'unknown': '#cccccc'
    }
    
    labels = list(severity_counts.keys())
    sizes = list(severity_counts.values())
    pie_colors = [colors.get(label, '#cccccc') for label in labels]
    
    plt.figure(figsize=(10, 8))
    wedges, texts, autotexts = plt.pie(sizes, labels=labels, colors=pie_colors, 
                                      autopct='%1.1f%%', startangle=90, 
                                      explode=[0.05] * len(labels))
    
    # Enhance text
    for text in texts:
        text.set_fontsize(12)
        text.set_fontweight('bold')
    
    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_fontweight('bold')
        autotext.set_color('white')
    
    plt.title('Security Issues Distribution by Severity Level', 
              fontsize=16, fontweight='bold', pad=20)
    
    # Add legend with counts
    legend_labels = [f'{label}: {count}' for label, count in severity_counts.items()]
    plt.legend(wedges, legend_labels, title="Severity Levels", 
               loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    
    plt.tight_layout()
    plt.savefig('sarif_severity_pie_chart.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_top_rules_pie_chart(results, top_n=10):
    """Create pie chart of top vulnerability rules"""
    rule_counts = Counter([r['rule_name'] for r in results])
    top_rules = dict(rule_counts.most_common(top_n))
    
    if not top_rules:
        return
    
    # If there are more rules, group the rest as "Others"
    total_issues = sum(rule_counts.values())
    top_issues = sum(top_rules.values())
    
    if total_issues > top_issues:
        top_rules['Others'] = total_issues - top_issues
    
    labels = list(top_rules.keys())
    sizes = list(top_rules.values())
    
    # Generate colors
    colors = plt.cm.Set3(np.linspace(0, 1, len(labels)))
    
    plt.figure(figsize=(14, 10))
    wedges, texts, autotexts = plt.pie(sizes, labels=labels, colors=colors,
                                      autopct='%1.1f%%', startangle=45)
    
    # Enhance text
    for text in texts:
        text.set_fontsize(10)
        text.set_fontweight('bold')
    
    for autotext in autotexts:
        autotext.set_fontsize(9)
        autotext.set_fontweight('bold')
        autotext.set_color('white')
    
    plt.title(f'Top {top_n} Security Rules by Number of Findings', 
              fontsize=16, fontweight='bold', pad=20)
    
    # Add legend with counts
    legend_labels = [f'{label}: {count}' for label, count in top_rules.items()]
    plt.legend(wedges, legend_labels, title="Security Rules", 
               loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    
    plt.tight_layout()
    plt.savefig('sarif_top_rules_pie_chart.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_cwe_pie_chart(results, top_n=8):
    """Create pie chart showing CWE distribution"""
    cwe_counts = Counter()
    
    for result in results:
        for tag in result['cwe_tags']:
            cwe_id = tag.replace('external/cwe/', '').upper()
            cwe_counts[cwe_id] += 1
    
    if not cwe_counts:
        print("No CWE tags found in the data")
        return
    
    top_cwes = dict(cwe_counts.most_common(top_n))
    
    # Group remaining as "Others" if any
    total_cwe_issues = sum(cwe_counts.values())
    top_cwe_issues = sum(top_cwes.values())
    
    if total_cwe_issues > top_cwe_issues:
        top_cwes['Others'] = total_cwe_issues - top_cwe_issues
    
    labels = list(top_cwes.keys())
    sizes = list(top_cwes.values())
    
    # Generate colors
    colors = plt.cm.Paired(np.linspace(0, 1, len(labels)))
    
    plt.figure(figsize=(12, 10))
    wedges, texts, autotexts = plt.pie(sizes, labels=labels, colors=colors,
                                      autopct='%1.1f%%', startangle=90,
                                      explode=[0.02] * len(labels))
    
    # Enhance text
    for text in texts:
        text.set_fontsize(11)
        text.set_fontweight('bold')
    
    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_fontweight('bold')
        autotext.set_color('white')
    
    plt.title(f'Top {top_n} CWE (Common Weakness Enumeration) Categories', 
              fontsize=16, fontweight='bold', pad=20)
    
    # Add legend with counts  
    legend_labels = [f'{label}: {count}' for label, count in top_cwes.items()]
    plt.legend(wedges, legend_labels, title="CWE Categories", 
               loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    
    plt.tight_layout()
    plt.savefig('sarif_cwe_pie_chart.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_security_severity_ranges_pie_chart(results):
    """Create pie chart showing security severity score ranges"""
    severity_ranges = {
        'Critical (9.0-10.0)': 0,
        'High (7.0-8.9)': 0, 
        'Medium (4.0-6.9)': 0,
        'Low (1.0-3.9)': 0,
        'Informational (0.1-0.9)': 0,
        'No Score (0.0)': 0
    }
    
    for result in results:
        score = result['security_severity']
        if score >= 9.0:
            severity_ranges['Critical (9.0-10.0)'] += 1
        elif score >= 7.0:
            severity_ranges['High (7.0-8.9)'] += 1
        elif score >= 4.0:
            severity_ranges['Medium (4.0-6.9)'] += 1
        elif score >= 1.0:
            severity_ranges['Low (1.0-3.9)'] += 1
        elif score > 0:
            severity_ranges['Informational (0.1-0.9)'] += 1
        else:
            severity_ranges['No Score (0.0)'] += 1
    
    # Filter out zero counts
    severity_ranges = {k: v for k, v in severity_ranges.items() if v > 0}
    
    if not severity_ranges:
        return
    
    labels = list(severity_ranges.keys())
    sizes = list(severity_ranges.values())
    
    # Define colors for severity ranges
    color_map = {
        'Critical (9.0-10.0)': '#8B0000',
        'High (7.0-8.9)': '#FF4500',
        'Medium (4.0-6.9)': '#FFA500', 
        'Low (1.0-3.9)': '#FFD700',
        'Informational (0.1-0.9)': '#90EE90',
        'No Score (0.0)': '#D3D3D3'
    }
    
    colors = [color_map.get(label, '#cccccc') for label in labels]
    
    plt.figure(figsize=(12, 10))
    wedges, texts, autotexts = plt.pie(sizes, labels=labels, colors=colors,
                                      autopct='%1.1f%%', startangle=90,
                                      explode=[0.05] * len(labels))
    
    # Enhance text
    for text in texts:
        text.set_fontsize(11)
        text.set_fontweight('bold')
    
    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_fontweight('bold')
        autotext.set_color('white')
    
    plt.title('Security Issues by Severity Score Ranges', 
              fontsize=16, fontweight='bold', pad=20)
    
    # Add legend with counts
    legend_labels = [f'{label}: {count}' for label, count in severity_ranges.items()]
    plt.legend(wedges, legend_labels, title="Severity Score Ranges", 
               loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    
    plt.tight_layout()
    plt.savefig('sarif_security_severity_ranges_pie_chart.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_combined_pie_charts(results):
    """Create a 2x2 subplot of different pie charts"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # 1. Severity distribution
    severity_counts = Counter([r['severity'] for r in results])
    if severity_counts:
        colors1 = ['#ff4444', '#ff8800', '#ffcc00', '#44ff44', '#cccccc']
        ax1.pie(severity_counts.values(), labels=severity_counts.keys(), 
                colors=colors1[:len(severity_counts)], autopct='%1.1f%%')
        ax1.set_title('Severity Distribution', fontweight='bold')
    
    # 2. Top 6 Rules
    rule_counts = Counter([r['rule_name'] for r in results])
    top_rules = dict(rule_counts.most_common(6))
    if top_rules:
        colors2 = plt.cm.Set3(np.linspace(0, 1, len(top_rules)))
        ax2.pie(top_rules.values(), labels=top_rules.keys(), 
                colors=colors2, autopct='%1.1f%%')
        ax2.set_title('Top 6 Security Rules', fontweight='bold')
    
    # 3. CWE Categories
    cwe_counts = Counter()
    for result in results:
        for tag in result['cwe_tags']:
            cwe_id = tag.replace('external/cwe/', '').upper()
            cwe_counts[cwe_id] += 1
    
    if cwe_counts:
        top_cwes = dict(cwe_counts.most_common(6))
        colors3 = plt.cm.Paired(np.linspace(0, 1, len(top_cwes)))
        ax3.pie(top_cwes.values(), labels=top_cwes.keys(), 
                colors=colors3, autopct='%1.1f%%')
        ax3.set_title('Top 6 CWE Categories', fontweight='bold')
    
    # 4. Security Severity Ranges
    severity_ranges = {'Critical': 0, 'High': 0, 'Medium': 0, 'Low': 0, 'Info': 0}
    for result in results:
        score = result['security_severity']
        if score >= 9.0:
            severity_ranges['Critical'] += 1
        elif score >= 7.0:
            severity_ranges['High'] += 1
        elif score >= 4.0:
            severity_ranges['Medium'] += 1
        elif score >= 1.0:
            severity_ranges['Low'] += 1
        else:
            severity_ranges['Info'] += 1
    
    severity_ranges = {k: v for k, v in severity_ranges.items() if v > 0}
    if severity_ranges:
        colors4 = ['#8B0000', '#FF4500', '#FFA500', '#FFD700', '#90EE90']
        ax4.pie(severity_ranges.values(), labels=severity_ranges.keys(), 
                colors=colors4[:len(severity_ranges)], autopct='%1.1f%%')
        ax4.set_title('Security Score Ranges', fontweight='bold')
    
    plt.suptitle('SARIF Security Analysis - Overview Dashboard', 
                 fontsize=18, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig('sarif_combined_pie_charts.png', dpi=300, bbox_inches='tight')
    plt.show()

def main():
    """Main function to generate all pie chart visualizations"""
    sarif_file = 'results_codeql.sarif'
    
    print("Loading SARIF file...")
    sarif_data = load_sarif_file(sarif_file)
    
    if not sarif_data:
        print("Failed to load SARIF file")
        return
    
    print("Extracting data...")
    results, rules_info = extract_sarif_data(sarif_data)
    
    if not results:
        print("No results found in SARIF file")
        return
    
    print(f"Found {len(results)} security findings")
    print(f"Found {len(rules_info)} security rules")
    
    # Set style for better looking plots
    plt.style.use('default')
    
    print("\nGenerating pie chart visualizations...")
    
    print("1. Creating severity pie chart...")
    create_severity_pie_chart(results)
    
    print("2. Creating top rules pie chart...")
    create_top_rules_pie_chart(results)
    
    print("3. Creating CWE distribution pie chart...")
    create_cwe_pie_chart(results)
    
    print("4. Creating security severity ranges pie chart...")
    create_security_severity_ranges_pie_chart(results)
    
    print("5. Creating combined dashboard...")
    create_combined_pie_charts(results)
    
    print("\nAll pie chart visualizations have been saved as PNG files!")
    print("Generated files:")
    print("- sarif_severity_pie_chart.png")
    print("- sarif_top_rules_pie_chart.png")
    print("- sarif_cwe_pie_chart.png")
    print("- sarif_security_severity_ranges_pie_chart.png")
    print("- sarif_combined_pie_charts.png")

if __name__ == "__main__":
    main()
