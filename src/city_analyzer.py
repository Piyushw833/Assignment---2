from typing import Dict, List, Any, Optional
from collections import defaultdict

class CityAnalyzer:
    """Pure Python class for analyzing city-wise insurance claims data."""
    
    def __init__(self, data: List[Dict[str, Any]]):
        """Initialize with a list of dictionaries containing claims data."""
        self.data = data
        
    def get_city_metrics(self) -> Dict[str, Dict[str, float]]:
        """Calculate key metrics for each city."""
        city_metrics = defaultdict(lambda: {
            'total_claims': 0,
            'total_claim_amount': 0.0,
            'total_premium': 0.0,
            'total_rejections': 0
        })
        
        # Calculate basic metrics
        for row in self.data:
            city = row.get('CITY', '')
            if not city:
                continue
                
            # Count claims
            city_metrics[city]['total_claims'] += 1
            
            # Sum claim amounts
            claim_amount = float(row.get('CLAIM_AMOUNT', 0) or 0)
            city_metrics[city]['total_claim_amount'] += claim_amount
            
            # Sum premiums
            premium = float(row.get('PREMIUM_COLLECTED', 0) or 0)
            city_metrics[city]['total_premium'] += premium
            
            # Count rejections
            if row.get('REJECTION_REMARKS'):
                city_metrics[city]['total_rejections'] += 1
        
        # Calculate derived metrics
        for city in city_metrics:
            metrics = city_metrics[city]
            
            # Calculate averages
            if metrics['total_claims'] > 0:
                metrics['avg_claim_amount'] = metrics['total_claim_amount'] / metrics['total_claims']
                metrics['avg_premium'] = metrics['total_premium'] / metrics['total_claims']
                metrics['rejection_rate'] = metrics['total_rejections'] / metrics['total_claims']
            else:
                metrics['avg_claim_amount'] = 0
                metrics['avg_premium'] = 0
                metrics['rejection_rate'] = 0
            
            # Calculate claim ratio
            if metrics['total_premium'] > 0:
                metrics['claim_ratio'] = metrics['total_claim_amount'] / metrics['total_premium']
            else:
                metrics['claim_ratio'] = 0
        
        return dict(city_metrics)
    
    def analyze_city_closure(self) -> Dict[str, Any]:
        """Analyze which city should be considered for closure."""
        metrics = self.get_city_metrics()
        
        # Calculate weighted score for each city
        weights = {
            'total_claims': -0.2,        # Higher claims = more important market
            'claim_ratio': 0.3,          # Higher ratio = more losses
            'rejection_rate': 0.2,       # Higher rejection rate = more operational issues
            'total_premium': -0.3        # Higher premium = more revenue
        }
        
        # Normalize metrics
        normalized_scores = {}
        for metric in weights.keys():
            values = [m[metric] for m in metrics.values()]
            min_val = min(values)
            max_val = max(values)
            range_val = max_val - min_val if max_val != min_val else 1
            
            for city in metrics:
                if city not in normalized_scores:
                    normalized_scores[city] = 0
                normalized_value = (metrics[city][metric] - min_val) / range_val
                normalized_scores[city] += normalized_value * weights[metric]
        
        # Get city with highest closure score
        recommended_city = max(normalized_scores.items(), key=lambda x: x[1])[0]
        
        return {
            'recommended_city': recommended_city,
            'city_scores': normalized_scores,
            'metrics': metrics,
            'reasoning': {
                'financial_impact': metrics[recommended_city]['total_premium'],
                'claim_ratio': metrics[recommended_city]['claim_ratio'],
                'rejection_rate': metrics[recommended_city]['rejection_rate'],
                'total_claims': metrics[recommended_city]['total_claims']
            }
        } 