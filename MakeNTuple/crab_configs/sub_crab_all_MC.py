if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from CRABClient.UserUtilities import config, getUsernameFromSiteDB
    from httplib import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config = config()
    config.section_("General")
    config.General.workArea = '/afs/cern.ch/work/m/mthiel/private/ANALYZER/Exclusive_VV_PPS/CMSSW1062_1209/CMSSW_10_6_2/src/MakeNTuple/MakeNTuple/crab_projects_MC/'
    config.General.transferOutputs = True
    config.General.transferLogs = False

    config.section_("JobType")
    config.JobType.pluginName = 'Analysis'
    config.JobType.psetName = 'ConfFile_MC_cfg.py'
    config.JobType.inputFiles = ['MyDataPileupHistogram.root','PileupMC.root']
    config.JobType.outputFiles = ['out.root']
    config.JobType.allowUndistributedCMSSW = True
   
    config.section_("Data")
#    config.Data.splitting = 'LumiBased' #LumiBased'
#    config.Data.unitsPerJob = 50
    config.Data.inputDBS = 'global'
    config.Data.splitting = 'Automatic' #'FileBased'
    config.Data.outLFNDirBase = '/store/user/mthiel' #%s/' % (getUsernameFromSiteDB())
    config.Data.publication = False
    config.Data.outputDatasetTag =  'background_3'

    config.section_("Site")
    config.Site.storageSite = "T2_CH_CERN"

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################


#example
#config.General.requestName = 'FSQJet1Bprompt'
#config.Data.inputDataset = '/FSQJet1/Run2018B-PromptReco-v2/MINIAOD'
#submit(config)


config.General.requestName = 'WJetsToLNu_Pt-600'
config.Data.inputDataset = '/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'WJetsToLNu_Pt-600_2'
config.Data.inputDataset = '/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'WJetsToLNu_Pt-400'
config.Data.inputDataset = '/WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'WJetsToLNu_Pt-400_2'
config.Data.inputDataset = '/WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'WJetsToLNu_Pt-250'
config.Data.inputDataset = '/WJetsToLNu_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext4-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'WJetsToLNu_Pt-250_2'
config.Data.inputDataset = '/WJetsToLNu_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM'
submit(config)

config.General.requestName = 'WJetsToLNu_Pt-250_3'
config.Data.inputDataset = '/WJetsToLNu_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'WJetsToLNu_Pt-100'
config.Data.inputDataset = '/WJetsToLNu_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext4-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'WJetsToLNu_Pt-100_2'
config.Data.inputDataset = '/WJetsToLNu_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'WJetsToLNu_Pt-100_3'
config.Data.inputDataset = '/WJetsToLNu_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'TT_TuneCUETP8M2T4'
config.Data.inputDataset = '/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'
submit(config)

config.General.requestName = 'DYJetsToLL_Pt-650'
config.Data.inputDataset = '/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'DYJetsToLL_Pt-650_2'
config.Data.inputDataset = '/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'DYJetsToLL_Pt-50'
config.Data.inputDataset = '/DYJetsToLL_Pt-50To100_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext3-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'DYJetsToLL_Pt-50_2'
config.Data.inputDataset = '/DYJetsToLL_Pt-50To100_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'DYJetsToLL_Pt-400'
config.Data.inputDataset = '/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'DYJetsToLL_Pt-400_2'
config.Data.inputDataset = '/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'DYJetsToLL_Pt-400_3'
config.Data.inputDataset = '/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'DYJetsToLL_Pt-250'
config.Data.inputDataset = '/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext5-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'DYJetsToLL_Pt-250_2'
config.Data.inputDataset = '/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'DYJetsToLL_Pt-250_3'
config.Data.inputDataset = '/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'DYJetsToLL_Pt-250_4'
config.Data.inputDataset = '/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'
submit(config)

config.General.requestName = 'DYJetsToLL_Pt-100'
config.Data.inputDataset = '/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext5-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'DYJetsToLL_Pt-100_2'
config.Data.inputDataset = '/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'DYJetsToLL_Pt-100_3'
config.Data.inputDataset = '/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM'
submit(config)

config.General.requestName = 'DYJetsToLL_Pt-100_4'
config.Data.inputDataset = '/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'QCD_Pt-800to1000_MuEnrichedPt5'
config.Data.inputDataset = '/QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'QCD_Pt-800to1000_MuEnrichedPt5_2'
config.Data.inputDataset = '/QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'QCD_Pt-800to1000_MuEnrichedPt5_3'
config.Data.inputDataset = '/QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'QCD_Pt-600to800_MuEnrichedPt5'
config.Data.inputDataset = '/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'QCD_Pt-600to800_MuEnrichedPt5_2'
config.Data.inputDataset = '/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'QCD_Pt-600to800_MuEnrichedPt5_3'
config.Data.inputDataset = '/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'QCD_Pt-470to600_MuEnrichedPt5'
config.Data.inputDataset = '/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'QCD_Pt-470to600_MuEnrichedPt5_2'
config.Data.inputDataset = '/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'QCD_Pt-470to600_MuEnrichedPt5_3'
config.Data.inputDataset = '/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'QCD_Pt-300to470_MuEnrichedPt5'
config.Data.inputDataset = '/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'QCD_Pt-300to470_MuEnrichedPt5_2'
config.Data.inputDataset = '/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM'
submit(config)

config.General.requestName = 'QCD_Pt-300to470_MuEnrichedPt5_3'
config.Data.inputDataset = '/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'QCD_Pt-170to300_MuEnrichedPt5'
config.Data.inputDataset = '/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'QCD_Pt-170to300_MuEnrichedPt5_2'
config.Data.inputDataset = '/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'QCD_Pt-170to300_MuEnrichedPt5_3'
config.Data.inputDataset = '/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'
submit(config)

config.General.requestName = 'QCD_Pt-1000toInf_MuEnrichedPt5'
config.Data.inputDataset = '/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'QCD_Pt-1000toInf_MuEnrichedPt5_2'
config.Data.inputDataset = '/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'QCD_Pt-300toInf_EMEnriched'
config.Data.inputDataset = '/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'QCD_Pt-170to300_EMEnriched'
config.Data.inputDataset = '/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'QCD_Pt-120to170_EMEnriched'
config.Data.inputDataset = '/QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'QCD_Pt-120to170_EMEnriched_2'
config.Data.inputDataset = '/QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'ST_s-channel'
config.Data.inputDataset = '/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'
submit(config)

config.General.requestName = 'ST_t-channel_antitop'
config.Data.inputDataset = '/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'
submit(config)

config.General.requestName = 'ST_t-channel_top'
config.Data.inputDataset = '/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'
submit(config)

config.General.requestName = 'ST_tW_top'
config.Data.inputDataset = '/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM'
submit(config)

config.General.requestName = 'ST_tW_antitop'
config.Data.inputDataset = '/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM'
submit(config)

config.General.requestName = 'WWToLNuQQ'
config.Data.inputDataset = '/WWToLNuQQ_13TeV-powheg/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'WWToLNuQQ_2'
config.Data.inputDataset = '/WWToLNuQQ_13TeV-powheg/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'WWToLNuQQ_3'
config.Data.inputDataset = '/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
submit(config)

config.General.requestName = 'ZZTo2L2Q'
config.Data.inputDataset = '/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'
submit(config)

config.General.requestName = 'ZZTo2L2Q_2'
config.Data.inputDataset = '/ZZTo2L2Q_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
submit(config)





