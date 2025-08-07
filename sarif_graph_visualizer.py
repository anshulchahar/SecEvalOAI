#!/usr/bin/env python3
"""
SARIF Graph Visualizer
Creates various graph visualizations from SARIF file data
"""

import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from collections import Counter, defaultdict
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

def create_severity_bar_chart(results):
    """Create bar chart showing severity distribution"""
    severity_counts = Counter([r['severity'] for r in results])
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(severity_counts.keys(), severity_counts.values(), 
                   color=['#ff4444', '#ff8800', '#ffcc00', '#44ff44'])
    plt.title('Security Issues by Severity Level', fontsize=16, fontweight='bold')
    plt.xlabel('Severity Level', fontsize=12)
    plt.ylabel('Number of Issues', fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('sarif_severity_bar_chart.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_security_severity_histogram(results):
    """Create histogram of security severity scores"""
    security_scores = [r['security_severity'] for r in results if r['security_severity'] > 0]
    
    plt.figure(figsize=(12, 6))
    plt.hist(security_scores, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title('Distribution of Security Severity Scores', fontsize=16, fontweight='bold')
    plt.xlabel('Security Severity Score (0-10)', fontsize=12)
    plt.ylabel('Number of Issues', fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    
    # Add statistics
    if security_scores:
        mean_score = np.mean(security_scores)
        plt.axvline(mean_score, color='red', linestyle='--', 
                   label=f'Mean: {mean_score:.1f}')
        plt.legend()
    
    plt.tight_layout()
    plt.savefig('sarif_security_severity_histogram.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_top_rules_chart(results):
    """Create horizontal bar chart of top vulnerability rules"""
    rule_counts = Counter([r['rule_name'] for r in results])
    top_rules = rule_counts.most_common(15)
    
    if not top_rules:
        return
    
    rules, counts = zip(*top_rules)
    
    plt.figure(figsize=(12, 8))
    bars = plt.barh(range(len(rules)), counts, color='lightcoral')
    plt.title('Top 15 Security Rules with Most Findings', fontsize=16, fontweight='bold')
    plt.xlabel('Number of Findings', fontsize=12)
    plt.ylabel('Security Rules', fontsize=12)
    plt.yticks(range(len(rules)), rules)
    plt.grid(axis='x', alpha=0.3)
    
    # Add value labels
    for i, bar in enumerate(bars):
        width = bar.get_width()
        plt.text(width + 0.1, bar.get_y() + bar.get_height()/2,
                f'{int(width)}', ha='left', va='center', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('sarif_top_rules_chart.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_cwe_distribution_chart(results):
    """Create chart showing CWE (Common Weakness Enumeration) distribution"""
    cwe_counts = Counter()
    
    for result in results:
        for tag in result['cwe_tags']:
            cwe_id = tag.replace('external/cwe/', '').upper()
            cwe_counts[cwe_id] += 1
    
    if not cwe_counts:
        print("No CWE tags found in the data")
        return
    
    top_cwes = cwe_counts.most_common(10)
    cwes, counts = zip(*top_cwes)
    
    plt.figure(figsize=(12, 8))
    bars = plt.bar(range(len(cwes)), counts, color='lightgreen')
    plt.title('Top 10 CWE (Common Weakness Enumeration) Categories', fontsize=16, fontweight='bold')
    plt.xlabel('CWE Categories', fontsize=12)
    plt.ylabel('Number of Issues', fontsize=12)
    plt.xticks(range(len(cwes)), cwes, rotation=45)
    plt.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('sarif_cwe_distribution_chart.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_severity_vs_security_score_scatter(results):
    """Create scatter plot of severity vs security score"""
    severity_mapping = {'error': 3, 'warning': 2, 'note': 1, 'info': 0, 'unknown': 0}
    
    x_values = []
    y_values = []
    colors = []
    
    for result in results:
        if result['security_severity'] > 0:
            x_values.append(severity_mapping.get(result['severity'], 0))
            y_values.append(result['security_severity'])
            colors.append(result['severity'])
    
    if not x_values:
        return
    
    plt.figure(figsize=(10, 8))
    
    # Create scatter plot with different colors for each severity
    for severity in set(colors):
        mask = [c == severity for c in colors]
        x_filtered = [x for x, m in zip(x_values, mask) if m]
        y_filtered = [y for y, m in zip(y_values, mask) if m]
        plt.scatter(x_filtered, y_filtered, label=severity, alpha=0.6, s=50)
    
    plt.title('Severity Level vs Security Severity Score', fontsize=16, fontweight='bold')
    plt.xlabel('Severity Level (0=info, 1=note, 2=warning, 3=error)', fontsize=12)
    plt.ylabel('Security Severity Score', fontsize=12)
    plt.legend()
    plt.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('sarif_severity_vs_security_scatter.png', dpi=300, bbox_inches='tight')
    plt.show()

def main():
    """Main function to generate all graph visualizations"""
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
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")
    
    print("\nGenerating visualizations...")
    
    print("1. Creating severity bar chart...")
    create_severity_bar_chart(results)
    
    print("2. Creating security severity histogram...")
    create_security_severity_histogram(results)
    
    print("3. Creating top rules chart...")
    create_top_rules_chart(results)
    
    print("4. Creating CWE distribution chart...")
    create_cwe_distribution_chart(results)
    
    print("5. Creating severity vs security score scatter plot...")
    create_severity_vs_security_score_scatter(results)
    
    print("\nAll graph visualizations have been saved as PNG files!")
    print("Generated files:")
    print("- sarif_severity_bar_chart.png")
    print("- sarif_security_severity_histogram.png") 
    print("- sarif_top_rules_chart.png")
    print("- sarif_cwe_distribution_chart.png")
    print("- sarif_severity_vs_security_scatter.png")

if __name__ == "__main__":
    main()
