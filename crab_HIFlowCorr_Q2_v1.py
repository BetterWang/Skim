from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

config = config()

config.General.requestName = 'HIFlowCorr_Q2Debug_T1030'
config.General.workArea = 'CrabArea'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'skimQ2_t1030_v1.py'
config.Data.inputDataset = '/HIFlowCorr/HIRun2015-PromptReco-v1/AOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 100
config.Data.outLFNDirBase = '/store/group/phys_heavyions/qwang/PbPb2015/'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/Cert_262548-263757_PromptReco_HICollisions15_JSON_v2.txt'
config.Site.storageSite = 'T2_CH_CERN'
# Top 1030
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)



config.General.requestName = 'HIFlowCorr_Q2Debug_B1030'
config.JobType.psetName = 'skimQ2_b1030_v1.py'
# Bot 1030
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


config.General.requestName = 'HIFlowCorr_Q2Debug_T3050'
config.JobType.psetName = 'skimQ2_t3050_v1.py'
# Top 3050
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIFlowCorr_Q2Debug_B3050'
config.JobType.psetName = 'skimQ2_b3050_v1.py'
# Bot 3050
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


config.General.requestName = 'HIFlowCorr_Q2Debug_T5070'
config.JobType.psetName = 'skimQ2_t5070_v1.py'
# Top 5070
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIFlowCorr_Q2Debug_B5070'
config.JobType.psetName = 'skimQ2_b5070_v1.py'
# Bot 5070
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

