from src.toontown.coghq.SpecImports import *
import random
GlobalEntities = {1000: {'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_11/models/lawbotHQ/LB_Zone22a',
        'wantDoors': 1},
 0: {'type': 'zone',
     'name': 'UberZone',
     'comment': '',
     'parentEntId': 0,
     'scale': 1,
     'description': '',
     'visibility': []},
 100030: {'type': 'battleBlocker',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-0.124318, -27.1644, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'cellId': 0,
          'radius': 25.0},
 100000: {'type': 'elevatorMarker',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(0.199988, -31.3479, 0),
          'hpr': Vec3(180, 0, 0),
          'scale': Point3(1, 1, 1),
          'modelPath': 0},
 100001: {'type': 'model',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(0, -30.3883, 13.5561),
          'hpr': Vec3(180, 0, 0),
          'scale': Vec3(2.6262, 2.6262, 2.6262),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_bookshelfB'},
 10000: {'type': 'nodepath',
         'name': 'cogs',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0, 0, 0),
         'hpr': Vec3(180, 0, 0),
         'scale': 1}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities,
 'scenarios': [Scenario0],
 'titleString': 'MemTag: LawbotOfficeOilRoom_Battle00 %s' % random.random()}