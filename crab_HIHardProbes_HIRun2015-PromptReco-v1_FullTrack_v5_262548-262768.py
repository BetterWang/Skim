from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'HIHardProbes_HIRun2015-PromptReco-v5_262548-262768'
config.General.workArea = 'CrabArea'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'skimFullTrack_v3.py'

config.Data.inputDataset = '/HIHardProbes/HIRun2015-PromptReco-v1/AOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 5
#config.Data.outLFNDirBase = '/store/group/phys_heavyions/qwang/Skim2015/'
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
#config.Data.outLFNDirBase = '/store/user/%s/HIHardProbes_HIRun2015-PromptReco-v1_FullTrack_v1' % (getUsernameFromSiteDB())
#config.Data.outLFNDirBase = '/store/group/phys_heavyions/qwang/'
config.Data.lumiMask = 'Cert_262548-262768_PromptReco_HICollisions15_JSON.txt'
#config.Data.runRange = '262538-262735'
config.Data.publication = True
config.Data.outputDatasetTag = 'HIHardProbes_FullTrackSkim2015_v5'
#config.Data.useParent = False

#config.Site.storageSite = 'T2_CH_CERN'
config.Site.storageSite = 'T2_US_MIT'

