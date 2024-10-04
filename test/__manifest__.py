{
    'name': 'Gestion des Tâches',
    'version': '1.0',
    'category': 'Productivity',
    'summary': 'Module de gestion des tâches permettant d\'ajouter des tâches et de voir la liste des tâches.',
    'description': """
        Ce module permet de gérer les tâches :
        - Ajouter une nouvelle tâche.
        - Voir la liste des tâches.
    """,
    'author': 'Creatic',
    'website': 'http://www.creatic.com',
    'depends': ['base','account'],
    'data': [
        'security/access_rights.csv',
        'security/ir.model.access.csv',  # Fichier pour définir les droits d'accès
        'views/compte_resultat.xml',
        'views/data.xml',
      
        
    ],
   

    'installable': True,
    'application': True,
    'auto_install': False,
}
