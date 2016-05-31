from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'HIHardProbes_HIRun2015-PromptReco-v5_263685-263757_TrackerCalo'
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
config.Data.lumiMask = 'Cert_263685-263757_PromptReco_HICollisions15_TrackerCaloBarrel_JSON.txt'
config.Data.runRange = '263685-263757'
config.Data.publication = True
config.Data.outputDatasetTag = 'HIHardProbes_FullTrackSkim2015_v5_TrackerCalo'
#config.Data.useParent = False

#config.Site.storageSite = 'T2_CH_CERN'
config.Site.storageSite = 'T2_US_MIT'

