"""
Wrapper for the Meraki Dashboard API.
"""
import meraki

class MerakiApiWrapper():
    """Wrapper for the Meraki Dashboard APIs."""

    def __init__(self, api_key, network_id):
        self.api_key = api_key
        self.network_id = network_id
        self.dashboard = meraki.DashboardAPI(
            api_key=api_key,
            base_url='https://api-mp.meraki.com/api/v0/',
            output_log=False)

    def get_rules(self):
        """Get the rules from the firewall."""
        mx_l3_firewall = self.dashboard.mx_l3_firewall
        return mx_l3_firewall.getNetworkL3FirewallRules(self.network_id)

    def update_rules(self, rules):
        """Upddate the rules in the firewall."""
        mx_l3_firewall = self.dashboard.mx_l3_firewall
        mx_l3_firewall.updateNetworkL3FirewallRules(self.network_id, rules=rules)
