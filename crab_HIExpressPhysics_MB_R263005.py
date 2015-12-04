from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'HIExpressPhysics_Run263005'
config.General.workArea = 'CrabArea'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'skimMBandExpress.py'

config.Data.inputDataset = '/HIExpressPhysics/HIRun2015-Express-v1/FEVT'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 2
config.Data.outLFNDirBase = '/store/group/phys_heavyions/qwang/Skim2015/'
config.Data.lumiMask = 'json_DCSONLY.txt'
config.Data.runRange = '263005'
config.Data.publication = False
config.Data.useParent = False

config.Site.storageSite = 'T2_CH_CERN'

