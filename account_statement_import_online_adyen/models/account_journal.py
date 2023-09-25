# Copyright 2021-2023 Therp BV <https://therp.nl>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api, models


class AccountJournal(models.Model):
    _inherit = "account.journal"

    @api.model
    def _selection_online_bank_statement_provider(self):
        res = super()._selection_online_bank_statement_provider()
        res.append(("dummy_adyen", "Dummy Adyen"))
        return res

    @api.model
    def values_online_bank_statement_provider(self):
        res = super().values_online_bank_statement_provider()
        if self.user_has_groups("base.group_no_one"):
            res += [("dummy_adyen", "Dummy Adyen")]
        return res
