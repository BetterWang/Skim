from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'HIHardProbes_HIRun2015-PromptReco-v1_FullTrack_v1'
config.General.workArea = 'CrabArea'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'skimFullTrack.py'

config.Data.inputDataset = '/HIHardProbes/HIRun2015-PromptReco-v1/AOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 10
#config.Data.outLFNDirBase = '/store/group/phys_heavyions/qwang/Skim2015/'
#config.Data.outLFNDirBase = '/store/user/%s/HIHardProbes_HIRun2015-PromptReco-v1_FullTrack_v1' % (getUsernameFromSiteDB())
config.Data.outLFNDirBase = '/store/group/phys_heavyions/qwang/HIHardProbes_HIRun2015-PromptReco-v1_FullTrack_v1'
config.Data.lumiMask = 'json_DCSONLY.txt'
config.Data.runRange = '262538-262726'
config.Data.publication = True
config.Data.useParent = False

config.Site.storageSite = 'T2_CH_CERN'
#config.Site.storageSite = 'T2_US_MIT'

