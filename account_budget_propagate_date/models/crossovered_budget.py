from odoo import models


class CrossoveredBudget(models.Model):
    _inherit = "crossovered.budget"

    def assign_budget_lines_dates(self):
        for line in self.crossovered_budget_line:
            line.date_from = self.date_from
            line.date_to = self.date_to
