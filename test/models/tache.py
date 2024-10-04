from odoo import models, fields, api

class Tache(models.Model):
    _name = 'tache'
    _description = 'Gestion des Tâches'

    nom_tache = fields.Char(string="Nom de la Tâche", required=True)
    date_debut_tache = fields.Date(string="Date de Début", required=True)
    duree_tache = fields.Float(string="Durée (en heures)", digits=(10, 5), required=True)
    status_tache = fields.Selection([
        ('0', 'Non commencé'),
        ('1', 'En cours'),
        ('2', 'Terminé')
    ], string="Statut", default='0', required=True)

    _order = 'id desc'

    def action_valider(self):
        for record in self:
            record.status_tache = '2'  # Set status to "Terminé"
  




from odoo import models, fields, api

class Annee(models.Model):
    _name = 'annee'
    _description = 'Année'

    annee_select = fields.Selection([
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026')
    ], string="Sélectionner l'année", default='2024', required=True)

    selected_year = fields.Char(string="Année Sélectionnée", compute='_compute_selected_year', store=False)

    @api.depends('annee_select')
    def _compute_selected_year(self):
        for record in self:
            record.selected_year = record.annee_select

    @api.onchange('annee_select')
    def _onchange_annee_select(self):
        # Mettre à jour le champ `selected_year` lors de la sélection
        self.selected_year = self.annee_select
    

