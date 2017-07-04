#include "newreg.inc"
#include "spr.inc"
#include "shm.inc"
#include "cond.inc"

// NOTE
// COND_STA_MODE is true in managed, monitor and ap mode, false in ad-hoc
// COND_AP_MODE is true in ap mode

#define ENABLE_PROMISC
#define noENABLE_RX_ALWAYS_IDLE

#define	BOBBIT	0x0040

	#define		T_DATA		0x02

	#define		TS_ACK			0x035
	#define		TS_BEACON		0x020
	#define		TS_PROBE_RESP		0x014
	#define		TS_PROBE_REQ		0x010
	#define		TS_RTS			0x02D
	#define		TS_CTS			0x031
	#define		TS_PSPOLL		0x029
	#define		TS_QOS_DATA		0x022
	#define		TS_ASSOC_REQ		0x000   
	#define		TS_REASSOC_REQ		0x008
	#define		TS_AUTH			0x02c

	#define         DEFAULT_MAX_CW		0x03FF
	#define         DEFAULT_MIN_CW		0x001F
	#define         DEFAULT_RETRY_LIMIT	7

#define	jump	\
	jext	COND_TRUE, 

#define	TXHDR(v)	[v,off0]

#define SETBIT(bit, dest)      \
	orxh    bit, dest & ~(bit), dest

#define SETBITMASK(bit, mask, dest)	\
	orxh	bit & mask, dest & ~mask, dest

#define CLEANBIT(bit, dest)    \
	orxh    0, dest & ~(bit), dest

#define SET_AND_CLEANBIT(bitset, bitclean, dest)	\
	orxh	bitset, dest & ~((bitset)|(bitclean)), dest

#define	SETBIT_MOV(bit, source, dest)	\
	orxh	bit, source & ~(bit), dest

#define MOV(val, dest)         \
	orx     7, 8, ( (val >> 8) ), ( (val & 0xFF) ), dest

#define MOV_WITH_OFFSET(val, offset, offreg)	\
	orx	7, 8, ( (val >> 8) &0xFF ), ( (val & 0xFF) ), [offset,offreg]

#define	BYTE_TO_WMMASK(byte)	\
	(1 << (byte/2))

#define MASK(cond)	(1 << (cond & 0xf))

	#define		MAC_CTL_RADIOLOCK		(1 << 3)
	#define		MAC_CTL_BEACON_PROMISC		(1 << 4)
	#define		MAC_CTL_KEEP_CTL		(1 << 6)
	#define		MAC_CTL_KEEP_BADFRAMES		(1 << 7)
	#define		MAC_CTL_PROMISCUOUS		(1 << 8)
	#define		MAC_CTL_DISCARD_TX_STATUS	(1 << 13)
	#define		MAC_CTL_GMODE			(1 << 15)

	#define		MAC_CMD_BEACON0_BUSY		(1 << 0)
	#define		MAC_CMD_BEACON1_BUSY		(1 << 1)
	#define		MAC_CMD_BEACON_BUSY_MASK	(MAC_CMD_BEACON0_BUSY|MAC_CMD_BEACON1_BUSY)
	#define		MAC_CMD_BGNOISE			(1 << 4)
	#define		MAC_CMD_ERASE_SHM		(1 << 5)

	#define		MAC_IRQHI_NOISE_SAMPLE_READY	(0x0004)
	#define		MAC_IRQLO_BEACON_AVAILABLE	(0x0002)

	#define		PHY_ROUTING_BASEBIT	10
	#define		PHY_REG_VERSION		0x0
	#define		PHY_CURRENT_CHAN	0x8
	#define		PHY_JSSI_NOISE_LO	0x27
	#define		PHY_RX_STATUS	0x5f

	#define		JSSIAUX_CHAN_MASK	0x00ff
	#define		JSSIAUX_STATUS_MASK	0xff00

	#define		IFS_STAT_MF_1SLOT	(1 << 2)
	#define		IFS_STAT_MF_2SLOT	(1 << 3)
	#define		IFS_STAT_TXING		(1 << 8)
	#define		IFS_STAT_RXING		(1 << 9)
	#define		IFS_STAT_RX_SIGDETEC	(1 << 11)

	#define		GFR1_G_MODE		(1 << 0)

	#define		GFR3_BEACON_BUSY_BASEBIT	7
	#define		GFR3_BEACON0_BUSY	(MAC_CMD_BEACON0_BUSY << GFR3_BEACON_BUSY_BASEBIT)
	#define		GFR3_BEACON1_BUSY	(MAC_CMD_BEACON1_BUSY << GFR3_BEACON_BUSY_BASEBIT)
	#define		GFR3_BEACON_BUSY_MASK	(MAC_CMD_BEACON_BUSY_MASK << GFR3_BEACON_BUSY_BASEBIT)
	#define		GFR3_DISCARD_FRAME_BIT	0
	#define		GFR3_DISCARD_FRAME	(1 << GFR3_DISCARD_FRAME_BIT)
	#define		GFR3_MEASURING_NOISE_BIT 3
	#define		GFR3_MEASURING_NOISE	(1 << GFR3_MEASURING_NOISE_BIT)
	#define		GFR3_FRAMEIS_WDS_BIT	11
	#define		GFR3_FRAMEIS_WDS	(1 << GFR3_FRAMEIS_WDS_BIT)

	#define		HF_ACPR		0x80



	#define		MAC_SUSPEND_TIMEOUT_8MHZ (35000*8)
	#define		TIMER_RUNNING	(0x8000)
	#define		TIMER_NOT_RUNNING (0x0000)
	#define		TIMER_8MHZ	(0x4000)
	#define		TIMER_88MHZ	(0x0000)
	#define		TIMER_RUNNING_8MHZ (TIMER_RUNNING| TIMER_8MHZ)

	#define		TXE0_SCHEDULE_WORKING	(0x001)

	#define		IHR_BUSY	(0x4000)
	#define		IHR_WRITE	(0x2000)
	#define		IHR_READ	(0x1000)

	#define		BEACON0_TEMPLATE_ADDR	0x0068
	#define		BEACON1_TEMPLATE_ADDR	0x0468

	#define	NEED_BEACON	(MASK(COND_NEED_BEACON))
	#define	NEED_RESPONSEFR	(MASK(COND_NEED_RESPONSEFR))
	#define	NEED_PROBE_RESP	(MASK(COND_NEED_PROBE_RESP))
	#define	CONTENTION_PARAM_MODIFIED	(MASK(COND_CONTENTION_PARAM_MODIFIED))
	#define	MORE_FRAGMENT	(MASK(COND_MORE_FRAGMENT))
	#define FRAME_BURST	(MASK(COND_FRAME_BURST))
	#define REC_IN_PROGRESS	(MASK(COND_REC_IN_PROGRESS))
	#define FRAME_NEED_ACK	(MASK(COND_FRAME_NEED_ACK))
	#define	TX_ERROR	(MASK(COND_TX_ERROR))
	#define	RX_ERROR	(MASK(COND_RX_ERROR))
	#define TX_MULTICAST_FRAME (MASK(COND_TX_MULTICAST_FRAME))
	#define NEED_RTS	(MASK(COND_NEED_RTS))
	#define PROBE_RESP_LOADED (MASK(COND_PROBE_RESP_LOADED))

	#define TXHDR_MACLO_USE_LONG_RETRY	2
	#define TXHDR_FCTL_NEED_ACK		1024

#define	LSW32(data)	(data & 0xFFFF)
#define HSW32(data)	((data >> 16) & 0xFFFF)

%arch 5

	MOV(0, SPR_GPIO_OUT)

// ***********************************************************************************************
// HANDLER:	init
// PURPOSE:	Initializes the device.
//
init:
	MOV(0, SPR_PSM_0x4e)
	MOV(0, SPR_PSM_0x0c)
	MOV(0x8000, SPR_SCC_Divisor)
	MOV(0x0002, SPR_SCC_Control)
	SETBIT(0x2, SPR_PHY_HDR_Parameter)
	jnzxh	SPR_MAC_CMD & MAC_CMD_ERASE_SHM, do_not_erase_shm
	mov	SHM_LAST_WORD, SPR_BASE5
erase_shm:
	MOV_WITH_OFFSET(0, 0x00, off5)
	sub	SPR_BASE5, 0x001, SPR_BASE5
	jges	SPR_BASE5, 0x000, erase_shm
do_not_erase_shm:
	MOV(1, [SHM_UCODESTAT])
	MOV(PHY_REG_VERSION, REG34)
	call	lr0, sel_phy_reg
	srxh	SPR_Ext_IHR_Data & 0xff, [SHM_PHYVER]
	srxh	(SPR_Ext_IHR_Data >> 8) & 0xf, [SHM_PHYTYPE]
	orx	7, 8, 0x000, 0x039, [0x0C0]
	orx	7, 8, 0x000, 0x050, [0x0C2]
	orx	7, 8, 0x0FC, 0x000, [SHM_PRPHYCTL]
	orx	7, 8, 0x000, 0x002, SPR_PHY_HDR_Parameter
	orx	7, 8, 0x000, 0x000, ANTENNA_DIVERSITY_CTR
	orx	7, 8, 0x000, 0x000, GPHY_SYM_WAR_FLAG
	orx	7, 8, 0x000, 0x000, GLOBAL_FLAGS_REG2
	orx	7, 8, 0x0FF, 0x000, [SHM_ACKCTSPHYCTL]
	orx	7, 8, 0x001, 0x09A, [SHM_UCODEREV]
	orx	7, 8, 0x008, 0x070, [SHM_UCODEPATCH]
	orx	7, 8, 0x075, 0x01A, [SHM_UCODEDATE]
	orx	7, 8, 0x07C, 0x00A, [SHM_UCODETIME]
	orx	7, 8, 0x000, 0x000, [SHM_PCTLWDPOS]
	orx	7, 8, 0x000, 0x000, [0x005]
	mov	SHM_RXHEADER, SPR_BASE1
	mov	SHM_TXHEADER, SPR_BASE0
	orx	7, 8, 0x000, 0x000, [SHM_FIFOCTL1_RESET]
	or	MIN_CONTENTION_WIN, 0x000, CUR_CONTENTION_WIN
	and	SPR_TSF_Random, MIN_CONTENTION_WIN, SPR_IFS_BKOFFDELAY
	MOV(TIMER_NOT_RUNNING| TIMER_8MHZ, SPR_TSF_GPT0_STAT)
	MOV(LSW32(MAC_SUSPEND_TIMEOUT_8MHZ), SPR_TSF_GPT0_CNTLO)
	MOV(HSW32(MAC_SUSPEND_TIMEOUT_8MHZ), SPR_TSF_GPT0_CNTHI)

	// if initvals do not, then let's do
	mov	0, SHORT_RETRIES
	mov	0, LONG_RETRIES
#define		DEFAULT_MAX_CW		0x03FF
	mov	DEFAULT_MAX_CW, MAX_CONTENTION_WIN
#define		DEFAULT_MIN_CW		0x001F
	mov	DEFAULT_MIN_CW, MIN_CONTENTION_WIN
#define DEFAULT_RETRY_LIMIT 7
	mov	DEFAULT_RETRY_LIMIT, SHORT_RETRY_LIMIT
	mov	DEFAULT_RETRY_LIMIT, LONG_RETRY_LIMIT
	jext	COND_TRUE, mac_suspend

// ***********************************************************************************************
// HANDLER:	state_machine_start
// PURPOSE:	Checks conditions looking for something to do. If there is no coming job firmware sleeps for a while or suspends device. 
//
state_machine_idle:
	jext	COND_PSM(0), state_machine_start

	jnzxh	GLOBAL_FLAGS_REG3 & GFR3_MEASURING_NOISE, state_machine_start
	MOV(0xFFFF, SPR_MAC_MAX_NAP)
	nap

state_machine_start:
	CLEANBIT(1, SPR_PSM_COND)

	// not sure if eoi can replace jnext other than jext
	extcond_eoi_only(COND_RADAR)
	extcond_eoi_only(COND_PHY0)
	extcond_eoi_only(COND_PHY1)
	jzxh	SPR_IFS_STAT & IFS_STAT_MF_1SLOT, dont_check_txe0_status
	jzxh	SPR_TXE0_STATUS & 1, reset_2us_waiting
dont_check_txe0_status:

	// check bit 0x0008, it is set by tx_timers_setup if rx needed
	jzxh	GLOBAL_FLAGS_REG2 & 8, reset_2us_waiting
	jdn	SPR_TSF_WORD0, [SHM_WAIT2_CLOCK], continue_2us_waiting

reset_2us_waiting:
	CLEANBIT(0x10|0x08, GLOBAL_FLAGS_REG2)

continue_2us_waiting:
	jzxh	SPR_IFS_STAT & IFS_STAT_MF_2SLOT, check_mac_status
	CLEANBIT(0x04|0x02, GLOBAL_FLAGS_REG2)
	or	[SHM_GCLASSCTL], 0x000, REG35
	call	lr1, gphy_classify_control_with_arg
check_mac_status:
	MOV(LSW32(MAC_SUSPEND_TIMEOUT_8MHZ), SPR_TSF_GPT0_VALLO)
	MOV(HSW32(MAC_SUSPEND_TIMEOUT_8MHZ), SPR_TSF_GPT0_VALHI)
	MOV(TIMER_RUNNING_8MHZ, SPR_TSF_GPT0_STAT)
	jnext	COND_MACEN, mac_suspend_check
check_conditions:
	jext	EOI(COND_TX_NOW), tx_frame_now
	jext	EOI(COND_TX_POWER), tx_infos_update
	jext	EOI(COND_TX_UNDERFLOW), Lrecode1
Lrecode1:
	jext	COND_TX_DONE, tx_end_wait_10us

check_conditions_no_tx:
	jext	COND_TX_PHYERR, tx_phy_error

check_rx_conditions:
	jzxh	SPR_BRWK0 & (MASK(COND_RX_IFS1)|MASK(COND_RX_IFS2)), skip_ifs_check

	jext	COND_RX_IFS2, prepare_to_set_ifs2
	jnext	COND_RX_IFS1, skip_ifs_check

	// for my memory: linksys in ap mode never gets here
prepare_to_set_ifs2:
	CLEANBIT((MASK(COND_RX_IFS1)|MASK(COND_RX_IFS2)), SPR_BRWK0)
	jext	COND_TRUE, set_ifs2

skip_ifs_check:
	jext	EOI(COND_RX_WME8), tx_timers_setup
	jext	EOI(COND_RX_PLCP), rx_plcp
	jext	COND_RX_COMPLETE, rx_complete
	jext	COND_TX_PMQ, tx_contention_params_update
	jext	EOI(COND_RX_BADPLCP), rx_badplcp
	jnext	COND_RX_FIFOFULL, rx_fifofull

	// only pccard execute the following (means: fifo can be full)
	jnext	COND_REC_IN_PROGRESS, rx_fifo_overflow

rx_fifofull:
	jnzxh	SPR_RXE_0x1a & 32768, rx_fifo_overflow
	extcond_eoi_only(COND_TX_NAV)
	jnext	COND_FRAME_NEED_ACK, channel_setup
	extcond_eoi_only(COND_PHY6)
	jext	COND_TRUE, state_machine_idle

/* --------------------------------------------------- HANDLERS ---------------------------------------------------------- */
// ***********************************************************************************************
// HANDLER:	channel_setup
// PURPOSE:	If TBTT expired prepares a beacon transmission else checks FIFO queue for incoming frames.	
//		The condition on SPR_BRC involves
//		COND_NEED_BEACON|COND_NEED_RESPONSEFR|COND_NEED_PROBE_RESP|COND_CONTENTION_PARAM_MODIFIED|COND_MORE_FRAGMENT
//
channel_setup:
	call	lr2, bg_noise_sample
	jext	COND_MORE_FRAGMENT, skip_beacon_ops
	jext	COND_TX_TBTTEXPIRE, prepare_beacon_tx

	jzxh	SPR_IFS_STAT & IFS_STAT_MF_1SLOT, no_gpio_hack
	jnzxh	SPR_TSF_GPT1_STAT & TIMER_RUNNING, no_gpio_hack
	jzxh	[SHM_HF_LO] & 16, no_gpio_hack

	// this is executed only on pccard
	orxh	0x0000, SPR_GPIO_OUT & ~0x0100, SPR_GPIO_OUT

no_gpio_hack:
	js	MAC_CMD_BEACON_BUSY_MASK, SPR_MAC_CMD, reset_mac_cmd_on_ap

skip_beacon_ops:
	extcond_eoi_only(COND_RX_ATIMWINEND)
	jand	SPR_TXE0_CTL, TXE0_SCHEDULE_WORKING, check_tx_data_with_disabled_engine		// jand jumps if the result is zero
check_tx_data:
	jext	EOI(COND_PHY6), check_tx_data
	jnand	(NEED_BEACON|NEED_RESPONSEFR|NEED_PROBE_RESP|CONTENTION_PARAM_MODIFIED|MORE_FRAGMENT), SPR_BRC, state_machine_idle				// jnand jumps if the result is non zero

	// no transmissions pending: check if slot end is likely approaching
	srxh	(SPR_IFS_0x0c >> 3) & 127, REG34
	jl	REG34, 0x004, state_machine_start				// if slot will end in less than 4 us do not sleep
	jext	COND_TRUE, state_machine_idle

	// for my memory: only aspirino_ap larrybird_ap panatta_ap get here
	// and larrybird_ap jumps immediately to state_machine_idle 
reset_mac_cmd_on_ap:
	jnand	FRAME_BURST, SPR_BRC, state_machine_idle

	srxh	(GLOBAL_FLAGS_REG3 >> GFR3_BEACON_BUSY_BASEBIT) & (GFR3_BEACON_BUSY_MASK >> GFR3_BEACON_BUSY_BASEBIT), REG34
	orxh	REG34 & MAC_CMD_BEACON_BUSY_MASK, 0x000, SPR_MAC_CMD
	MOV(MAC_IRQLO_BEACON_AVAILABLE, SPR_MAC_IRQLO)
	srxh	SPR_MAC_CMD & MAC_CMD_BEACON_BUSY_MASK, REG34
	orxh	(REG34 << GFR3_BEACON_BUSY_BASEBIT ) & GFR3_BEACON_BUSY_MASK, GLOBAL_FLAGS_REG3 & ~GFR3_BEACON_BUSY_MASK, GLOBAL_FLAGS_REG3
	jext	COND_TRUE, state_machine_idle

// ***********************************************************************************************
// HANDLER:	prepare_beacon_tx
// PURPOSE:	Prepares parameters (PHY and MAC) needed for a correct Beacon transmission.
//		The condition on SPR_BRC involves
//		COND_NEED_BEACON|COND_NEED_RESPONSEFR|COND_FRAME_BURST|COND_REC_IN_PROGRESS|COND_FRAME_NEED_ACK
//
prepare_beacon_tx:
	jnand	(NEED_BEACON|NEED_RESPONSEFR|FRAME_BURST|REC_IN_PROGRESS|FRAME_NEED_ACK), SPR_BRC, state_machine_idle
	jnzxh	GLOBAL_FLAGS_REG2 & 4, state_machine_idle
	jext	COND_PSM(1), state_machine_start

	jzxh	[SHM_HF_LO] & 16, no_gpio_hack2

	// run only on pccard
	orxh	0x0100, SPR_GPIO_OUT & ~0x0100, SPR_GPIO_OUT

no_gpio_hack2:
	jnext	COND_STA_MODE, beacon_tx_param_update
	jext	COND_AP_MODE, beacon_tx_param_update

	// run only on STA
inhibit_sleep_call:
	call	lr0, inhibit_sleep_at_tbtt
	jext	COND_TRUE, state_machine_idle

	// run only on AP
beacon_tx_param_update:
	jzxh	SPR_MAC_CMD & MAC_CMD_BEACON_BUSY_MASK, inhibit_sleep_call
	call	lr0, flush_and_stop_tx_engine
	or	[SHM_BEACPHYCTL], 0x000, SPR_TXE0_PHY_CTL
bcn_no_hw_pwr_ctl:
	call	lr1, prep_phy_txctl_encoding_already_set
	orx	7, 8, 0x000, 0x020, TX_TYPE_SUBTYPE
	call	lr3, LABEL559
	jext	COND_CONTENTION_PARAM_MODIFIED, skip_parameter_preservation
	orx	7, 8, 0x000, 0x004, SPR_MAC_IRQLO
	orx	7, 8, 0x000, 0x000, SPR_TSF_Random
skip_parameter_preservation:
	or	[SHM_BTSFOFF], 0x000, SPR_TSF_0x3a
	SET_AND_CLEANBIT(NEED_BEACON, NEED_RESPONSEFR|NEED_PROBE_RESP, SPR_BRC)
	SETBIT(CONTENTION_PARAM_MODIFIED, SPR_BRC)
goto_set_ifs:
	orx	7, 8, 0x049, 0x083, SPR_TXE0_CTL
	jext	COND_TRUE, state_machine_idle

// ***********************************************************************************************
// HANDLER:	check_tx_data
// PURPOSE:	Checks if there is a frame into the FIFO queue. If a frame is incoming from host loads BCM
//		header into SHM and analyzes frame properties, then prepares PHY and MAC parameters for transmission.
//		This code should be invoke with TX engine disabled.
//		The condition on SPR_BRC involves
//		COND_NEED_BEACON|COND_NEED_RESPONSEFR|COND_NEED_PROBE_RESP|COND_CONTENTION_PARAM_MODIFIED|COND_FRAME_BURST
//
check_tx_data_with_disabled_engine:
	jext	COND_PSM(1), state_machine_start
	extcond_eoi_only(COND_PHY6)
	jnand	NEED_BEACON|NEED_RESPONSEFR|NEED_PROBE_RESP|CONTENTION_PARAM_MODIFIED|FRAME_BURST, SPR_BRC, state_machine_idle
	jext	COND_TX_NOW, state_machine_start
	jnzxh	SPR_TXE0_STATUS & 1, ready_for_header_copy

	// for my memory: only linksys in STA mode get here
	CLEANBIT(MORE_FRAGMENT, SPR_BRC)
	jext	COND_TRUE, state_machine_idle

ready_for_header_copy:
	jzxh	SPR_MAC_CMD & 4, slow_clock_control
	jzxh	SPR_TXE0_FIFO_RDY & 2, slow_clock_control
	orx	2, 8, 0x001, 0x000, [SHM_TXFCUR]
copy_header_into_shm:
	call	lr3, load_tx_header_into_shm
	jext	COND_TRUE, check_tx_channel

check_tx_channel:
	srxh	([TXHDR_MACLO,off0] >> 7) & 3, REG34
	srxh	([TXHDR_EFT,off0] >> 8) & 255, REG35
	orxh	(REG34 << 8) & 0x0300, REG35 & ~0x0300, REG34
	srxh	[SHM_CHAN] & 1023, REG35
	je	REG34, REG35, check_pmq_tx_header_info

	// only STAs get here
	orxh	0x0010, [TXHDR_STAT,off0] & ~0x001C, [TXHDR_STAT,off0]
	jext	COND_TRUE, suppress_this_frame

check_pmq_tx_header_info:
	or	[TXHDR_PHYCTL,off0], 0x000, SPR_TXE0_PHY_CTL
	jext	COND_MORE_FRAGMENT, skip_pmq_op
	jnand	[TXHDR_MACLO,off0], 0x020, skip_pmq_op
	or	[TXHDR_RA,off0], 0x000, SPR_PMQ_pat_0
	or	[TXHDR_PMQ1,off0], 0x000, SPR_PMQ_pat_1
	or	[TXHDR_PMQ2,off0], 0x000, SPR_PMQ_pat_2
	orx	7, 8, 0x000, 0x004, SPR_PMQ_control_low
skip_pmq_op:
	orxh	0x0004, [TXHDR_HK5,off0] & ~0x0006, [TXHDR_HK5,off0]
	jext	COND_MORE_FRAGMENT, extract_phy_info
	or	[TXHDR_FES,off0], 0x000, SPR_TX_FES_Time
	jzxh	[TXHDR_HK5,off0] & 16, dont_set_fallback_fes_time
	or	[TXHDR_FESFB,off0], 0x000, SPR_TX_FES_Time
dont_set_fallback_fes_time:
	jnzxh	[TXHDR_MACLO,off0] & 32, extract_phy_info
wait_pmq_to_clean:
	jnzxh	SPR_PMQ_control_low & 4, wait_pmq_to_clean
extract_phy_info:
	jnzxh	[TXHDR_HK5,off0] & 16, extract_fallback_info
	srxh	[TXHDR_PHYRATES,off0] & 255, REG0
	srxh	[TXHDR_PHYCTL,off0] & 3, REG1
	jext	COND_TRUE, extract_tx_type_subtype
extract_fallback_info:
	srxh	[TXHDR_PLCPFB0,off0] & 255, REG0
	srxh	[TXHDR_EFT,off0] & 3, REG1
extract_tx_type_subtype:
	srxh	([TXHDR_FCTL,off0] >> 2) & 63, TX_TYPE_SUBTYPE
	call	lr1, get_ptr_from_rate_table
check_tx_no_hw_pwr_ctl:
	call	lr1, prep_phy_txctl_with_encoding
	srxh	(SPR_TXE0_PHY_CTL >> 4) & 1, REG1
	orxh	(REG1 << 4) & 0x0010, [SHM_CURMOD] & ~0x0010, REG1
	call	lr0, get_rate_table_duration
	add	REG34, [SHM_SLOTT], REG34
	orxh	(REG34 << 3) & 0x7FF8, 0x000 & ~0x7FF8, SPR_TXE0_TIMEOUT
	call	lr3, LABEL559

check_tx_next_txe_ctl_1:
	orx	7, 8, 0x04C, 0x01D, NEXT_TXE0_CTL
	jne	TX_TYPE_SUBTYPE, TS_PROBE_RESP, check_tx_next_txe_ctl_2

	// only AP get here
	// but I think after removing probe response offloading it will
	// not get here anymore
	orx	7, 8, 0x04D, 0x01D, NEXT_TXE0_CTL
check_tx_next_txe_ctl_2:
	jext	COND_TRUE, set_ifs

// ***********************************************************************************************
// HANDLER:	suppress_this_frame
// PURPOSE:	Flushes frame and tells the host that transmission failed.
//
// Only STAs may suppress frame, AP never
suppress_this_frame:
	orx	7, 8, 0x000, 0x000, SPR_TXE0_SELECT
	jext	COND_TRUE, report_tx_status_to_host

// ***********************************************************************************************
// HANDLER:	set_ifs
// PURPOSE:	Prepares backoff time (if it is equal to zero) for the next contention stage.
// 
set_ifs:
	extcond_eoi_only(COND_RX_ATIMWINEND)
	orx	7, 8, 0x000, 0x001, [0x042]
	or	NEXT_TXE0_CTL, 0x000, SPR_TXE0_CTL
	jne	SPR_IFS_BKOFFDELAY, 0x000, state_machine_idle
set_ifs2:
	jext	COND_RX_IFS1, go_with_ifs1
	jext	COND_RX_IFS2, go_with_ifs2
	orxh	0x0006, SPR_BRWK0 & ~0x0006, SPR_BRWK0
	jext	COND_TRUE, state_machine_idle
go_with_ifs2:
	jext	EOI(COND_TX_NOW), tx_frame_now
go_with_ifs1:
	orx	7, 8, 0x000, 0x000, SPR_TSF_Random
	call	lr1, set_backoff_time
	jext	COND_TRUE, state_machine_idle

// ***********************************************************************************************
// HANDLER:	tx_frame_now
// PURPOSE:	Performs a data, ACK or Beacon frame transmission according to the PHY and MAC parameters that have been set.
//
tx_frame_now:
	orx	7, 8, 0x000, 0x004, SPR_RXE_FIFOCTL1
	nand	SPR_BRC, (TX_ERROR|FRAME_NEED_ACK), SPR_BRC
	orx	7, 8, 0x083, 0x000, SPR_WEP_CTL
	jzxh	[SHM_HF_LO] & 16, no_gpio_hack3
	// only pc card get here
	jnzxh	GLOBAL_FLAGS_REG2 & 32, no_gpio_hack3
	orxh	0x0100, SPR_GPIO_OUT & ~0x0100, SPR_GPIO_OUT
no_gpio_hack3:
	CLEANBIT(0x8000, GLOBAL_FLAGS_REG1)
	jne	[0x042], 0x001, no_param_update_needed
	or	SPR_TSF_WORD0, 0x000, [0x043]
no_param_update_needed:
	orxh	FRAME_BURST, SPR_BRC & ~ FRAME_BURST, SPR_BRC
	orxh	0x0010, SPR_IFS_CTL & ~0x0010, SPR_IFS_CTL
	orxh	0x0000, SPR_BRWK0 & ~0x0006, SPR_BRWK0
	orx	7, 8, 0x000, 0x000, SPR_TXE0_WM0
	orx	7, 8, 0x000, 0x000, SPR_TXE0_WM1
	jnext	COND_NEED_RESPONSEFR, tx_beacon_or_data
	orx	7, 8, 0x000, 0x0FF, SPR_TXE0_WM0
	srxh	(GLOBAL_FLAGS_REG3 >> 5) & 1, REG34
	orxh	(REG34 << 12) & 0x1000, SPR_TME_VAL6 & ~0x1000, SPR_TME_VAL6
	jles	SPR_TME_VAL8, 0x000, dont_update_preamble
	sub	SPR_TME_VAL8, [SHM_PREAMBLE_DURATION], SPR_TME_VAL8
	jzxh	SPR_TXE0_PHY_CTL & 16, dont_use_short_preamble

	// only AP get here (till next label)
	sr	[SHM_PREAMBLE_DURATION], 0x001, REG34
	add	SPR_TME_VAL8, REG34, SPR_TME_VAL8
dont_use_short_preamble:
	jges	SPR_TME_VAL8, 0x000, dont_update_preamble

	// only AP execute the following line
	orx	7, 8, 0x000, 0x000, SPR_TME_VAL8
dont_update_preamble:
	orx	7, 8, 0x000, 0x000, SPR_TXE0_SELECT
	orx	7, 8, 0x000, 0x000, SPR_TXE0_Template_TX_Pointer
	orx	7, 8, 0x000, 0x010, SPR_TXE0_TX_COUNT
	orx	7, 8, 0x008, 0x026, SPR_TXE0_SELECT
	jext	COND_TRUE, complete_tx

tx_beacon_or_data:
	jnext	COND_NEED_BEACON, tx_data

	// the following is executed only on AP, tx a beacon
	orxh	0x0000, SPR_BRC & ~ CONTENTION_PARAM_MODIFIED, SPR_BRC

	// this can be: jump if beacon is untouch, or actually it doesn't jump at all
	jnext	COND_STA_MODE, dont_touch_beacon

	jgs	CURRENT_DTIM_COUNTER, 0x000, dont_update_tim_counter
	or	[SHM_DTIMPER], 0x000, CURRENT_DTIM_COUNTER
dont_update_tim_counter:
	sub	CURRENT_DTIM_COUNTER, 0x001, CURRENT_DTIM_COUNTER
	orx	7, 8, 0x000, 0x000, REG35
	jgs	CURRENT_DTIM_COUNTER, 0x000, load_beacon_tim
	srxh	(SPR_TXE0_FIFO_RDY >> 4) & 1, REG35
	orxh	(REG35 << 10) & TX_MULTICAST_FRAME, SPR_BRC & ~ TX_MULTICAST_FRAME, SPR_BRC
load_beacon_tim:
	orxh	0x0002, SPR_TXE0_AUX & ~0x0002, SPR_TXE0_AUX
	orx	7, 8, 0x004, 0x06A, REG34
	add	REG34, [SHM_TIMBPOS], REG34

	mov	SHM_BEACON_TIM_PTR, SPR_BASE5
	sl	SPR_BASE5, 0x001, SPR_TXE0_TX_SHM_ADDR
	orx	7, 8, 0x000, 0x000, SPR_TXE0_SELECT
	orxh	0x0000, REG34 & ~0x0003, SPR_TXE0_Template_TX_Pointer
	orx	7, 8, 0x000, 0x008, SPR_TXE0_TX_COUNT
	orx	7, 8, 0x008, 0x005, SPR_TXE0_SELECT

wait_tx_bcn_free:
	jnext	COND_TX_BUSY, wait_tx_bcn_free
wait_tx_bcn_write:
	jext	COND_TX_BUSY, wait_tx_bcn_write
	orxh	(CURRENT_DTIM_COUNTER << 0) & 0x00FF, [0x00,off5] & ~0x00FF, [0x00,off5]
	orxh	(REG35 << 0) & 0x0001, [0x01,off5] & ~0x0001, [0x01,off5]
end_dtim_update:
	orxh	0x0000, REG34 & ~0x0003, SPR_TXE0_Template_Pointer
	or	[0x00,off5], 0x000, SPR_TXE0_Template_Data_Low
	or	[0x01,off5], 0x000, SPR_TXE0_Template_Data_High
wait_tmpl_ram:
	jnzxh	SPR_TXE0_Template_Pointer & 1, wait_tmpl_ram
	add	SPR_TXE0_Template_Pointer, 0x004, SPR_TXE0_Template_Pointer
	or	[0x02,off5], 0x000, SPR_TXE0_Template_Data_Low
	or	[0x03,off5], 0x000, SPR_TXE0_Template_Data_High

	// only on AP
dont_touch_beacon:
	SETBIT(BYTE_TO_WMMASK(28), SPR_TXE0_WM0)
	add	SEQUENCE_CTR, 0x001, SEQUENCE_CTR
	orxh	(SEQUENCE_CTR << 4) & 0xFFF0, 0x000 & ~0xFFF0, SPR_TME_VAL28

	MOV(0, SPR_TXE0_SELECT)

	MOV(BEACON0_TEMPLATE_ADDR, SPR_TXE0_Template_TX_Pointer)
	mov	[SHM_BTL0], SPR_TXE0_TX_COUNT
	jnzxh	GLOBAL_FLAGS_REG3 & GFR3_BEACON0_BUSY, beacon_template_selected

	MOV(BEACON1_TEMPLATE_ADDR, SPR_TXE0_Template_TX_Pointer)
	mov	[SHM_BTL1], SPR_TXE0_TX_COUNT

beacon_template_selected:
	orx	7, 8, 0x008, 0x026, SPR_TXE0_SELECT
	SETBIT(BOBBIT, GLOBAL_FLAGS_REG3)
	extcond_eoi_only(COND_TX_TBTTEXPIRE)

no_params_preservation:
	or	MIN_CONTENTION_WIN, 0x000, CUR_CONTENTION_WIN
	jnzxh	SPR_TSF_0x0e & 1, params_restored
	and	SPR_TSF_Random, CUR_CONTENTION_WIN, SPR_IFS_BKOFFDELAY

params_restored:
	orx	7, 8, 0x000, 0x008, SPR_MAC_IRQLO
	orxh	0x0010, GLOBAL_FLAGS_REG3 & ~0x0010, GLOBAL_FLAGS_REG3
complete_tx:
	orx	0, 8, 0x001, 0x000, SPR_WEP_CTL
	jext	COND_NEED_BEACON, update_txe_timeout
	jext	COND_TRUE, update_txe_timeout2
tx_data:
	srxh	([TXHDR_MACLO,off0] >> 6) & 1, REG34
	xor	REG34, 0x001, REG34
	orxh	(REG34 << 14) & 0x4000, SPR_TXE0_CTL & ~0x4000, SPR_TXE0_CTL
	jext	COND_NEED_PROBE_RESP, force_fallback_updates
	jzxh	[TXHDR_HK5,off0] & 16, no_fallback_updates
force_fallback_updates:
	or	[TXHDR_PLCPFB0,off0], 0x000, SPR_TME_VAL0
	or	[TXHDR_PLCPFB1,off0], 0x000, SPR_TME_VAL2
	or	[TXHDR_DURFB,off0], 0x000, SPR_TME_VAL8
	or	SPR_TXE0_WM0, 0x013, SPR_TXE0_WM0
no_fallback_updates:
	orxh	0x4000, [SHM_TXFCUR] & ~0x4000, SPR_TXE0_FIFO_CMD
	or	[SHM_TXFCUR], 0x000, SPR_TXE0_SELECT
	orx	7, 8, 0x000, 0x068, SPR_TXE0_TX_COUNT
	or	[SHM_TXFCUR], 0x007, SPR_TXE0_SELECT
	orxh	0x0002, [SHM_TXFCUR] & ~0x0003, SPR_TXE0_SELECT
	srxh	TX_TYPE_SUBTYPE & 3, REG34
	je	REG34, 0x001, dont_update_seq_ctr_value_for_control_frame
	jnzxh	[TXHDR_STAT,off0] & 61440, update_seq_ctr_value
	jzxh	[TXHDR_MACLO,off0] & 8, update_seq_ctr_value
	add	SEQUENCE_CTR, 0x001, SEQUENCE_CTR
	srxh	SEQUENCE_CTR & 4095, [TXHDR_RTSSEQCTR,off0]
update_seq_ctr_value:
	orxh	([TXHDR_RTSSEQCTR,off0] << 4) & 0xFFF0, 0x000 & ~0xFFF0, SPR_TME_VAL28
	orxh	0x4000, SPR_TXE0_WM0 & ~0x4000, SPR_TXE0_WM0
dont_update_seq_ctr_value_for_control_frame:
	srxh	(SPR_MAC_CTLHI >> 9) & 1, REG34
	orxh	(REG34 << 5) & 0x0020, GLOBAL_FLAGS_REG3 & ~0x0020, GLOBAL_FLAGS_REG3
tx_frame_update_status_info:
	orxh	(REG34 << 7) & 0x0080, [TXHDR_STAT,off0] & ~0x0080, [TXHDR_STAT,off0]
	orxh	(REG34 << 12) & 0x1000, 0x000 & ~0x1000, SPR_TME_VAL6
	orx	0, 12, 0x001, 0x000, SPR_TME_MASK6
	orxh	0x0008, SPR_TXE0_WM0 & ~0x0008, SPR_TXE0_WM0
	srxh	TX_TYPE_SUBTYPE & 3, REG34
	je	REG34, 0x001, tx_frame_analysis
	jzxh	[TXHDR_STAT,off0] & 61440, update_gpreg5_with_cur_fifo
	orxh	0x0800, SPR_TME_VAL6 & ~0x0800, SPR_TME_VAL6
	orxh	0x0800, SPR_TME_MASK6 & ~0x0800, SPR_TME_MASK6
update_gpreg5_with_cur_fifo:
	srxh	([SHM_TXFCUR] >> 8) & 7, REG34
tx_frame_analysis:
	orx	0, 8, 0x001, 0x000, SPR_WEP_CTL
find_tx_frame_type:
	orx	7, 8, 0x000, 0x000, SPR_TSF_Random
	or	SPR_TSF_0x40, 0x000, [TXHDR_RTSPLCP,off0]
	orx	7, 8, 0x000, 0x000, EXPECTED_CTL_RESPONSE
	je	TX_TYPE_SUBTYPE, 0x02D, LABEL182
	jzxh	[TXHDR_MACLO,off0] & 1, reset_cur_contention_window
LABEL182:
	orxh	FRAME_NEED_ACK, SPR_BRC & ~ FRAME_NEED_ACK, SPR_BRC
	or	SPR_BRC, 0x000, 0x000
	orx	7, 8, 0x000, 0x031, EXPECTED_CTL_RESPONSE
	je	TX_TYPE_SUBTYPE, 0x02D, update_txe_timeout2
	orx	7, 8, 0x000, 0x035, EXPECTED_CTL_RESPONSE
	jext	COND_TRUE, update_txe_timeout2
reset_cur_contention_window:
	or	MIN_CONTENTION_WIN, 0x000, CUR_CONTENTION_WIN
	call	lr1, set_backoff_time
update_txe_timeout:
	orx	7, 8, 0x000, 0x000, SHORT_RETRIES
	orx	7, 8, 0x000, 0x000, LONG_RETRIES
update_txe_timeout2:
	jnext	COND_FRAME_NEED_ACK, dont_update_txe_timeout
	orxh	0x8000, SPR_TXE0_TIMEOUT & ~0x8000, SPR_TXE0_TIMEOUT
dont_update_txe_timeout:
no_radar_war:
tx_frame_no_B_phy:
	je	[SHM_PHYTYPE], 0x000, tx_frame_A_phy
	jnzxh	SPR_TXE0_PHY_CTL & 3, tx_frame_A_phy
	add	SPR_TSF_WORD0, 0x028, REG34
	jext	COND_TRUE, tx_frame_wait_16us
tx_frame_A_phy:
	add	SPR_TSF_WORD0, 0x010, REG34
tx_frame_wait_16us:
	jext	COND_TX_DONE, state_machine_idle
	jne	SPR_TSF_WORD0, REG34, tx_frame_wait_16us
	jnzxh	SPR_TXE0_PHY_CTL & 1, aphy_tssi_selection
	orx	7, 8, 0x000, 0x029, REG34
	mov	SHM_TSSI_CCK_LO, SPR_BASE5
	jext	COND_TRUE, update_phy_params
aphy_tssi_selection:
	orx	7, 8, 0x004, 0x07B, REG34
	mov	SHM_TSSI_OFDM_G_LO, SPR_BASE5
update_phy_params:
	call	lr0, sel_phy_reg
	rr	[0x01,off5], 0x008, [0x01,off5]
	srxh	([0x00,off5] >> 8) & 255, REG34
	orxh	(REG34 << 0) & 0x00FF, [0x01,off5] & ~0x00FF, [0x01,off5]
	rr	[0x00,off5], 0x008, [0x00,off5]
	orxh	(SPR_Ext_IHR_Data << 0) & 0x00FF, [0x00,off5] & ~0x00FF, [0x00,off5]

tx_frame_no_cca_in_progress:
	jnzxh	SPR_IFS_STAT & IFS_STAT_RX_SIGDETEC, state_machine_idle
	jge	SPR_NAV_0x04, 0x0A0, state_machine_idle
	orx	7, 8, 0x0FF, 0x0FF, SPR_NAV_0x04
	orx	0, 10, 0x001, 0x05F, REG34
wait_for_ihr_data_to_clear:
	call	lr0, sel_phy_reg
	and	SPR_Ext_IHR_Data, 0x01F, REG35
	je	REG35, 0x016, wait_for_ihr_data_to_clear
	orx	7, 8, 0x000, 0x000, SPR_NAV_0x04
	jext	COND_TRUE, state_machine_idle

// ***********************************************************************************************
// HANDLER:	tx_infos_update
// PURPOSE:	Updates retries informations and looks for transmission error. If sent frame doesn't require ACK, tells the host that transmission was successfully performed.
// NEED_RESPONSEFR is true if we transmitted an ack, so we don't need to report anything to host!!
// FRAME_NEED_ACK is true if we transmitted something and we wait for the ack. For traffic
//                that does not need ack, report status immediately
//
tx_infos_update:
	CLEANBIT(FRAME_BURST, SPR_BRC)
	mov	0x8700, SPR_WEP_CTL
	jnzxh	[TXHDR_FCTL,off0] & TXHDR_FCTL_NEED_ACK, need_ack
	CLEANBIT(MORE_FRAGMENT, SPR_BRC)
need_ack:
	jext	COND_NEED_RESPONSEFR, need_response_frame
	extcond_eoi_only(COND_TX_UNDERFLOW)
	jext	EOI(COND_TX_PHYERR), tx_clear_issues
	jnext	COND_NEED_BEACON, dont_need_beacon
	// glad to see that only AP may not jump from the jump above

need_response_frame:
	CLEANBIT(NEED_BEACON|NEED_RESPONSEFR, SPR_BRC)
	jump	state_machine_start

dont_need_beacon:
	MOV(0x1, REG34)
	srxh	(TXHDR(TXHDR_STAT) >> 12) & 0xF, REG11
	add	REG11, REG34, REG11
	orxh	(REG11 << 12) & 0xF000, TXHDR(TXHDR_STAT) & 0x0FFF, TXHDR(TXHDR_STAT)

	jext	COND_FRAME_NEED_ACK, state_machine_start
	jext	COND_TRUE, report_tx_status_to_host

// ***********************************************************************************************
// HANDLER:	tx_end_wait_10us
// PURPOSE:	Called at the end of a transmission. It will be called
//		for 8us, after that noise will be measured and stored in SHM_PHYTXNOI.
//		
//
tx_end_wait_10us:
	jnzxh	GLOBAL_FLAGS_REG1 & 0x10, tx_end_completed
	SETBIT(0x10, GLOBAL_FLAGS_REG1)
	mov	SPR_TSF_WORD0, [SHM_WAIT10_CLOCK]
	MOV(TIMER_NOT_RUNNING|TIMER_8MHZ, SPR_TSF_GPT2_STAT)
	call	lr3, LABEL559
tx_end_completed:
	sub	SPR_TSF_WORD0, [SHM_WAIT10_CLOCK], REG38
	jl	REG38, 0x008, check_conditions_no_tx
	orx	7, 8, 0x000, 0x027, REG34
	call	lr0, sel_phy_reg
	and	SPR_Ext_IHR_Data, 0x0FF, [SHM_PHYTXNOI]
	CLEANBIT(0x10, GLOBAL_FLAGS_REG1)
	jext	EOI(COND_TX_DONE), state_machine_idle
	jext	COND_TRUE, report_tx_status_to_host

// ***********************************************************************************************
// HANDLER:	report_tx_status_to_host
// PURPOSE:	Reports informations about transmission to the host, informing it about success or failure of the operation.
//
// In 5.2 there was an entry point to handle RTS, I removed it
report_tx_status_to_host:
	jand	[TXHDR_HK4,off0], 0x003, dont_clear_housekeeping
	jnext	EOI(COND_RX_FIFOFULL), rx_fifo_not_full

	// for my memory this line is needed only for pccard
	orxh	([SHM_FIFOCTL1_RESET] << 8) & 0x0300, 0x014 & ~0x0300, SPR_RXE_FIFOCTL1
	jext	COND_TRUE, rx_fifo_handled

rx_fifo_not_full:
	jext	COND_RX_FIFOBUSY, report_tx_status_to_host
	jext	COND_RX_CRYPTBUSY, report_tx_status_to_host
rx_fifo_handled:
	orx	7, 8, 0x000, 0x000, [TXHDR_RTS,off0]
	orxh	0x2000, [SHM_TXFCUR] & ~0x2000, SPR_TXE0_FIFO_CMD
	jzxh	[TXHDR_STAT,off0] & 1, rise_status_interrupt
	or	SPR_RXE_PHYRXSTAT1, 0x000, [TXHDR_RTS,off0]
rise_status_interrupt:
	orx	7, 8, 0x000, 0x080, SPR_MAC_IRQLO
	jnzxh	SPR_MAC_CTLHI & MAC_CTL_DISCARD_TX_STATUS, discard_tx_status
	or	[TXHDR_STAT,off0], 0x000, REG34
	orxh	(REG34 << 1) & 0x0002, REG34 & ~0x0002, REG34
	or	[TXHDR_RTSPHYSTAT,off0], 0x000, SPR_TX_STATUS3
	or	[TXHDR_RTSSEQCTR,off0], 0x000, SPR_TX_STATUS2
	or	[TXHDR_COOKIE,off0], 0x000, SPR_TX_STATUS1
	orxh	0x0001, REG34 & ~0x0001, SPR_TX_STATUS0
discard_tx_status:
	orxh	0x0000, [TXHDR_HK4,off0] & ~0x0003, [TXHDR_HK4,off0]
dont_clear_housekeeping:
	orxh	0x0000, [TXHDR_STAT,off0] & ~0x0040, [TXHDR_STAT,off0]
	orxh	0x0000, SPR_BRC & ~ NEED_RTS, SPR_BRC
	orx	7, 8, 0x000, 0x000, [TXHDR_RTSPHYSTAT,off0]
	jext	COND_MORE_FRAGMENT, check_tx_data_with_disabled_engine
	jext	COND_TRUE, state_machine_start

// ***********************************************************************************************
// HANDLER:	tx_contention_params_update
// PURPOSE:	Updates current window parameter according to success or failure of transmission operation. Checks if retries reached the top limit and eventually commands a drop operation.
//
tx_contention_params_update:
	jnext	COND_FRAME_NEED_ACK, finish_updates
	jext	COND_REC_IN_PROGRESS, finish_updates
	jext	COND_FRAME_BURST, finish_updates

	CLEANBIT(FRAME_NEED_ACK, SPR_BRC)

	jnext	EOI(COND_TX_PMQ), reset_antenna_ctr_if_needed
	// TBA secondo me il bit 2 di GFR2 non e' mai settato, da verificare
	jnzxh	GLOBAL_FLAGS_REG2 & 2, update_params_on_success
	add	[0x09A], 0x001, [0x09A]
	jext	COND_TRUE, update_contention_params
reset_antenna_ctr_if_needed:
	jnext	COND_RX_FCS_GOOD, dont_reset_antenna_ctr
	je	RX_TYPE_SUBTYPE, TS_CTS, dont_reset_antenna_ctr
	orx	7, 8, 0x000, 0x000, ANTENNA_DIVERSITY_CTR
dont_reset_antenna_ctr:
	jext	COND_TX_ERROR, update_contention_params
	jext	EOI(COND_RX_FCS_GOOD), update_params_on_success
update_contention_params:
	CLEANBIT(TX_ERROR, SPR_BRC)
	call	lr1, antenna_diversity_helper
	CLEANBIT(MORE_FRAGMENT, SPR_BRC)
	orxh	(CUR_CONTENTION_WIN << 1) & 0xFFFE, 0x001, CUR_CONTENTION_WIN
	and	CUR_CONTENTION_WIN, MAX_CONTENTION_WIN, CUR_CONTENTION_WIN
	je	EXPECTED_CTL_RESPONSE, TS_CTS, using_fallback
	jnzxh	[TXHDR_MACLO,off0] & TXHDR_MACLO_USE_LONG_RETRY, use_long_retry

using_fallback:
	or	SHORT_RETRY_LIMIT, 0x000, REG36
	or	[SHM_SFFBLIM], 0x000, REG37
	jl	REG11, REG37, dont_use_fallback_short
	SETBIT(0x0010, TXHDR(TXHDR_HK5))

dont_use_fallback_short:
	add	SHORT_RETRIES, 0x001, SHORT_RETRIES
	jne	SHORT_RETRIES, REG36, short_retry_limit_not_reached_yet
	// only the pc with the pccard execute the following
	or	MIN_CONTENTION_WIN, 0x000, CUR_CONTENTION_WIN
short_retry_limit_not_reached_yet:
	jge	REG11, REG36, retry_limit_reached
	jext	COND_TRUE, retry_limit_not_reached
use_long_retry:
	or	LONG_RETRY_LIMIT, 0x000, REG36
	or	[SHM_LFFBLIM], 0x000, REG37
	jl	REG11, REG37, dont_use_fallback_long
	orxh	0x0010, [TXHDR_HK5,off0] & ~0x0010, [TXHDR_HK5,off0]
dont_use_fallback_long:
	add	LONG_RETRIES, 0x001, LONG_RETRIES
	jne	LONG_RETRIES, REG36, long_retry_limit_not_reached_yet
	or	MIN_CONTENTION_WIN, 0x000, CUR_CONTENTION_WIN
long_retry_limit_not_reached_yet:
	jl	REG11, REG36, retry_limit_not_reached
retry_limit_reached:
	extcond_eoi_only(COND_TX_PMQ)
	call	lr1, set_backoff_time
	orxh	0x0008, [TXHDR_HK5,off0] & ~0x0008, [TXHDR_HK5,off0]
	orxh	0x0000, SPR_BRC & ~ NEED_RTS, SPR_BRC
	jext	COND_TRUE, report_tx_status_to_host
retry_limit_not_reached:
	call	lr1, set_backoff_time
	orxh	0x0000, SPR_BRC & ~ NEED_PROBE_RESP, SPR_BRC
	orxh	0x0000, SPR_BRC & ~ PROBE_RESP_LOADED, SPR_BRC
finish_updates:
	extcond_eoi_only(COND_TX_PMQ)
	jext	COND_NEED_RTS, report_tx_status_to_host
	jext	COND_TRUE, state_machine_start
update_params_on_success:
	srxh	TX_TYPE_SUBTYPE & 3, REG34
	je	REG34, 0x001, update_params_control_frame
	or	MIN_CONTENTION_WIN, 0x000, CUR_CONTENTION_WIN
update_params_control_frame:
	call	lr1, set_backoff_time
	orx	7, 8, 0x000, 0x000, SHORT_RETRIES
	jzxh	[TXHDR_MACLO,off0] & 2, use_short_retry
	orx	7, 8, 0x000, 0x000, LONG_RETRIES
use_short_retry:
	orxh	0x0001, [TXHDR_STAT,off0] & ~0x0001, [TXHDR_STAT,off0]
	jext	COND_TRUE, report_tx_status_to_host

// ***********************************************************************************************
// HANDLER:	send_response
// PURPOSE:	Sends an ACK back to the station whose MAC was contained in the source address header field.
//		At the end set the NEED_RESPONSEFR bit in SPR_BRC that will trigger the condition COND_NEED_RESPONSEFR
//		that will be evaluated at next tx_frame_now
//		Values are taken from the tables in initvals.asm
//		e.g. for CCK
//		1Mb/s	(A)	off5=37E
//		2Mb/s	(4)	off5=389
//		5.5Mb/s	(7)	off5=394
//		11Mb/s	(E)	off5=39F
//
send_response:
	jext	COND_RX_ERROR, rx_complete
	orx	7, 8, 0x000, 0x00E, REG34
	mov	[0x01,off2], SPR_TME_VAL0
	je	[SHM_CURMOD], 0x000, cck_mod
	orxh	(REG34 << 5) & 0xFFE0, [0x01,off2] & ~0xFFE0, SPR_TME_VAL0
cck_mod:
	or	[0x02,off2], 0x000, SPR_TME_VAL2
	orx	7, 8, 0x000, 0x000, SPR_TME_VAL4
	mov	[RX_FRAME_ADDR2_1,off1], SPR_TME_VAL10
	orx	7, 8, 0x0FF, 0x0FF, SPR_TME_MASK10
	mov	[RX_FRAME_ADDR2_2,off1], SPR_TME_VAL12
	orx	7, 8, 0x0FF, 0x0FF, SPR_TME_MASK12
	mov	[RX_FRAME_ADDR2_3,off1], SPR_TME_VAL14
	orx	7, 8, 0x0FF, 0x0FF, SPR_TME_MASK14
	mov	[SHM_ACKCTSPHYCTL], SPR_TXE0_PHY_CTL
no_hw_pwr_ctl:
	srxh	[SHM_CURMOD] & 3, REG1
	call	lr1, prep_phy_txctl_with_encoding
	call	lr3, LABEL559
	orxh	0x0004, GLOBAL_FLAGS_REG1 & ~0x0004, GLOBAL_FLAGS_REG1
	orx	7, 8, 0x0FF, 0x0FF, SPR_TME_MASK6
	orx	7, 8, 0x000, 0x0D4, SPR_TME_VAL6
	orx	7, 8, 0x000, 0x035, TX_TYPE_SUBTYPE
	je	RX_TYPE_SUBTYPE, TS_PSPOLL, pspoll_frame
ctl_more_frag:
	or	[SHM_CURMOD], 0x000, REG1
	call	lr0, get_rate_table_duration
	sub	REG34, [SHM_PREAMBLE_DURATION], REG34
	jgs	REG34, [RX_FRAME_DURATION,off1], pspoll_frame
	sub	[RX_FRAME_DURATION,off1], REG34, SPR_TME_VAL8
	jext	COND_TRUE, trigger_cts_ack_transmission
pspoll_frame:
	orx	7, 8, 0x000, 0x000, SPR_TME_VAL8
trigger_cts_ack_transmission:
	orxh	NEED_RESPONSEFR, SPR_BRC & ~ (NEED_BEACON|NEED_RESPONSEFR|NEED_PROBE_RESP), SPR_BRC
sym_war_txe_ctl:
	mov	0x4021, NEXT_TXE0_CTL
send_response_end:
	je	RX_TYPE_SUBTYPE, TS_RTS, send_control_frame_to_host
	jext	COND_RX_COMPLETE, rx_complete
	jext	COND_TRUE, state_machine_idle

// ***********************************************************************************************
// HANDLER:	tx_timers_setup
// PURPOSE:	Updates timers informations.
//
// Cleans bit 0x0018 of GLOBAL_FLAGS_REG2. Then if no update needed, exits.
// If update needed, start waiting 2us in state_machine_start.
// If needed by RX clean bit 0x0010 and set bit 0x0008 of GLOBAL_FLAGS_REG2.
// When state_machine_start finishes waiting 2 us, then it will clean bit 0x0018
// of GLOBAL_FLAGS_REG2.
//
tx_timers_setup:
	jzxh	SPR_BRPO0 & 0x0100, proceed_with_timer_update
	CLEANBIT(0x10|0x08, GLOBAL_FLAGS_REG2)
	CLEANBIT(0x100, SPR_BRPO0)
	CLEANBIT(TIMER_RUNNING, SPR_TSF_GPT0_STAT)
	SETBIT(TIMER_RUNNING, SPR_TSF_GPT0_STAT)
	jext	COND_TRUE, state_machine_idle
proceed_with_timer_update:
	jnzxh	SPR_IFS_STAT & IFS_STAT_RX_SIGDETEC, timers_update_goon
	SETBIT(0x100, SPR_BRPO0)
	jzxh	GLOBAL_FLAGS_REG2 & 0x40, timers_update_goon

	// only STA get here
	call	lr2, LABEL588

timers_update_goon:
	MOV(TIMER_NOT_RUNNING|TIMER_8MHZ, SPR_TSF_GPT2_STAT)
	add	SPR_TSF_WORD0, 0x002, [SHM_WAIT2_CLOCK]
	jnzxh	SPR_RXE_0x1a & 0x80, state_machine_start
	orxh	0x08, GLOBAL_FLAGS_REG2 & ~(0x10|0x08), GLOBAL_FLAGS_REG2

	jext	COND_TRUE, state_machine_start

// ***********************************************************************************************
// HANDLER:	rx_plcp
// PURPOSE:	If header was successfully received, extracts from it frame related informations.
//		Current time is stored inside four registers RX_TIME_WORD[0-3]
//		RX_PHY_ENCODING stores the kind of encoding for all the succeeding analysis: 0 is CCK, 1 is OFDM
//		At the beginning switch off the TX engine if it is not
//
rx_plcp:
	jext	EOI(COND_RX_FCS_GOOD), rx_plcp
	orx	7, 8, 0x000, 0x000, GPHY_SYM_WAR_FLAG
	jnzxh	SPR_RXE_FIFOCTL1 & 4, state_machine_idle
	jzxh	SPR_TXE0_CTL & 1, sync_rx_frame_time_with_TSF
	orx	7, 8, 0x000, 0x000, SPR_TXE0_CTL
	orxh	0x0000, SPR_BRC & ~ (NEED_BEACON|NEED_RESPONSEFR|NEED_PROBE_RESP), SPR_BRC
sync_rx_frame_time_with_TSF:
	or	SPR_TSF_WORD0, 0x000, LAST_RX_TIME_WORD0
	or	SPR_TSF_WORD1, 0x000, LAST_RX_TIME_WORD1
	or	SPR_TSF_WORD2, 0x000, LAST_RX_TIME_WORD2
	or	SPR_TSF_WORD3, 0x000, LAST_RX_TIME_WORD3
	jne	LAST_RX_TIME_WORD0, SPR_TSF_WORD0, sync_rx_frame_time_with_TSF
	add	[0x088], 0x001, [0x088]
	srxh	(SPR_RXE_ENCODING >> 13) & 1, REG23
rx_plcp_not_A_phy:
	orx	7, 8, 0x000, 0x008, REG34
	call	lr0, sel_phy_reg
	srxh	([SHM_CHAN] >> 8) & 1, REG34
	orxh	(REG34 << 8) & 0x0100, SPR_Ext_IHR_Data & ~0x0100, REG34
	orxh	(REG34 << 3) & 0x1FF8, [SHM_PHYTYPE] & ~0x1FF8, [SHM_RXHDR_RXCHAN]
	or	SPR_BRC, (TX_ERROR|REC_IN_PROGRESS), SPR_BRC
	orxh	0x0000, SPR_BRC & ~ (RX_ERROR), SPR_BRC
	orxh	0x0000, GLOBAL_FLAGS_REG3 & ~ GFR3_DISCARD_FRAME, GLOBAL_FLAGS_REG3
wait_for_header_to_be_received:
	jext	COND_RX_COMPLETE, header_received
	jl	SPR_RXE_FRAMELEN, 0x026, wait_for_header_to_be_received
header_received:
	orx	7, 8, 0x000, 0x000, [SHM_RXHDR_MACST_LOW]
	orx	7, 8, 0x000, 0x000, [SHM_RXHDR_MACST_HIGH]
	jl	SPR_RXE_FRAMELEN, 0x010, rx_too_short
	srxh	([RX_FRAME_FC,off1] >> 2) & 63, RX_TYPE_SUBTYPE
	srxh	([RX_FRAME_FC,off1] >> 2) & 3, RX_TYPE
	orxh	0x0000, GLOBAL_FLAGS_REG3 & ~0x3000, GLOBAL_FLAGS_REG3
	srxh	([RX_FRAME_FC,off1] >> 8) & 1, REG34
	srxh	([RX_FRAME_FC,off1] >> 9) & 1, REG35
	and	REG34, REG35, REG35
	orxh	(REG35 << GFR3_FRAMEIS_WDS_BIT) & GFR3_FRAMEIS_WDS, GLOBAL_FLAGS_REG3 & ~ GFR3_FRAMEIS_WDS, GLOBAL_FLAGS_REG3
	and	RX_TYPE_SUBTYPE, 0x023, REG34
	jne	REG34, TS_QOS_DATA, not_qos_data
	orxh	0x1000, GLOBAL_FLAGS_REG3 & ~0x1000, GLOBAL_FLAGS_REG3
	xor	REG35, 0x001, REG35
	add	SPR_BASE1, SHM_PLCP_MAC3ADDR_HDR_SIZE, SPR_BASE5
	jzxh	GLOBAL_FLAGS_REG3 & GFR3_FRAMEIS_WDS, rx_plcp_not_wds
	add	SPR_BASE5, SHM_MAC_ADDR_SIZE, SPR_BASE5
rx_plcp_not_wds:
	or	[0x00,off5], 0x000, REG33
	jzxh	[0x00,off5] & 96, not_qos_data
	orxh	0x2000, GLOBAL_FLAGS_REG3 & ~0x2000, GLOBAL_FLAGS_REG3
not_qos_data:
	orxh	(REG35 << 5) & 0x0020, 0x000 & ~0x0020, SPR_RXE_FIFOCTL1
	jext	COND_RX_RAMATCH, rx_plcp_and_ra_match
	jnzxh	[RX_FRAME_DURATION,off1] & 32768, check_frame_version_validity
	or	[RX_FRAME_DURATION,off1], 0x000, SPR_NAV_ALLOCATION
	orxh	0x1000, SPR_NAV_CTL & ~0xF800, SPR_NAV_CTL
	jext	COND_TRUE, check_frame_version_validity
rx_plcp_and_ra_match:
	jzxh	[SHM_HF_LO] & 16, check_frame_version_validity
	// only on pccard
	orxh	0x0100, SPR_GPIO_OUT & ~0x0100, SPR_GPIO_OUT
check_frame_version_validity:
	jzxh	[RX_FRAME_FC,off1] & 3, disable_crypto_engine
	orxh	GFR3_DISCARD_FRAME, GLOBAL_FLAGS_REG3 & ~ GFR3_DISCARD_FRAME, GLOBAL_FLAGS_REG3
	jext	COND_TRUE, rx_too_short
disable_crypto_engine:
	orx	7, 8, 0x083, 0x000, SPR_WEP_CTL
	orxh	0x0002, SPR_RXE_FIFOCTL1 & ~0x0003, SPR_RXE_FIFOCTL1
	je	RX_TYPE_SUBTYPE, TS_ACK, rx_plcp_not_data_frame
	srxh	[RX_FRAME_PLCP_0,off1] & 255, REG0
	or	REG23, 0x000, REG1
	call	lr1, get_ptr_from_rate_table
	jne	RX_TYPE, 0x002, rx_plcp_not_data_frame
	jext	COND_TRUE, rx_data_plus
rx_plcp_not_data_frame:
	jext	COND_RX_FIFOFULL, rx_fifo_overflow
	jnzxh	SPR_RXE_0x1a & 32768, rx_fifo_overflow_pre
	jnext	COND_RX_COMPLETE, rx_plcp_not_data_frame
rx_plcp_wait_RXE_x1a:
	jzxh	SPR_RXE_0x1a & 16384, rx_plcp_wait_RXE_x1a
	srxh	(SPR_RXE_PHYRXSTAT0 >> 5) & 1, [SHM_LAST_RX_ANTENNA]
	jg	SPR_RXE_FRAMELEN, [SHM_MAXPDULEN], rx_complete
	jext	COND_RX_FCS_GOOD, rx_plcp_good_fcs
	call	lr1, check_gphy_sym_war
	je	GPHY_SYM_WAR_FLAG, 0x000, rx_complete
rx_plcp_good_fcs:
	jne	RX_TYPE, 0x000, rx_plcp_control_frame
	je	RX_TYPE_SUBTYPE, TS_BEACON, rx_beacon_probe_resp
	je	RX_TYPE_SUBTYPE, TS_PROBE_RESP, rx_beacon_probe_resp
	je	RX_TYPE_SUBTYPE, TS_PROBE_REQ, send_response_if_ra_match
	jext	COND_TRUE, send_response_if_ra_match
rx_plcp_control_frame:
	je	RX_TYPE_SUBTYPE, TS_ACK, rx_ack
	je	RX_TYPE_SUBTYPE, TS_CTS, rx_ack
	je	RX_TYPE_SUBTYPE, TS_PSPOLL, rx_check_promisc
	jext	COND_TRUE, send_control_frame_to_host

// ***********************************************************************************************
// HANDLER:	rx_too_short
// PURPOSE:	Reports reception error and checks if frame must be kept.
//	
// XXX need rework to report short frames..
rx_too_short:
	orxh	RX_ERROR, SPR_BRC & ~ RX_ERROR, SPR_BRC
	jext	COND_TRUE, disable_crypto_engine

// ***********************************************************************************************
// HANDLER:	rx_complete
// PURPOSE:	Completes reception and classifies frame. 
//
rx_complete:
clear_rxe_x1a:
	jzxh	SPR_RXE_0x1a & 16384, clear_rxe_x1a
	or	SPR_TSF_0x3e, 0x000, [SHM_RXHDR_MACTIME]
	orxh	0x0000, SPR_BRC & ~ REC_IN_PROGRESS, SPR_BRC
wait_for_rec_completion:
	jnext	EOI(COND_RX_COMPLETE), wait_for_rec_completion
	jnzxh	SPR_RXE_0x1a & 32768, rx_fifo_overflow_pre
	jg	SPR_RXE_FRAMELEN, [SHM_MAXPDULEN], rx_too_long
	jext	COND_RX_FCS_GOOD, frame_successfully_received
	jne	GPHY_SYM_WAR_FLAG, 0x000, frame_successfully_received
	orxh	RX_ERROR, SPR_BRC & ~ RX_ERROR, SPR_BRC
	orxh	0x0000, SPR_BRC & ~ NEED_RESPONSEFR, SPR_BRC
	jext	COND_RX_FIFOFULL, rx_fifo_overflow
	orxh	0x0001, [SHM_RXHDR_MACST_LOW] & ~0x0001, [SHM_RXHDR_MACST_LOW]
	orxh	GFR3_DISCARD_FRAME, GLOBAL_FLAGS_REG3 & ~ GFR3_DISCARD_FRAME, GLOBAL_FLAGS_REG3
	jext	COND_TRUE, send_frame_to_host
frame_successfully_received:
	jext	COND_RX_FIFOFULL, rx_fifo_overflow
	jnext	COND_NEED_RESPONSEFR, check_frame_subtype
need_regular_ack:
	je	[SHM_CURMOD], 0x001, ofdm_modulation
	jne	[SHM_CURMOD], 0x000, no_cck_modulation
	jzxh	[0x01,off2] & 240, ofdm_modulation
no_cck_modulation:
	srxh	(SPR_RXE_PHYRXSTAT0 >> 7) & 1, REG34
	orxh	(REG34 << 4) & 0x0010, SPR_TXE0_PHY_CTL & ~0x0010, SPR_TXE0_PHY_CTL
ofdm_modulation:
	orxh	0x0002, [SHM_RXHDR_MACST_LOW] & ~0x0002, [SHM_RXHDR_MACST_LOW]
	or	NEXT_TXE0_CTL, 0x000, SPR_TXE0_CTL
check_frame_subtype:
	srxh	RX_TYPE_SUBTYPE & 3, REG34
	je	REG34, 0x001, rx_control_frame
	jext	COND_RX_RAMATCH, rx_frame_and_ra_match
	jzxh	[RX_FRAME_ADDR1_1,off1] & 1, not_multicast_frame
	jne	RX_TYPE, T_DATA, rx_not_data_frame_type
	add	[0x094], 0x001, [0x094]
rx_not_data_frame_type:
	jnzxh	GLOBAL_FLAGS_REG3 & GFR3_FRAMEIS_WDS, send_frame_to_host
	jnzxh	[RX_FRAME_FC,off1] & 256, discard_frame
	jnzxh	[RX_FRAME_FC,off1] & 512, control_frame_from_ds
	jext	COND_RX_BSSMATCH, frame_from_our_BSS
	jext	COND_TRUE, could_be_multicast_frame
control_frame_from_ds:
	jnext	0x62, could_be_multicast_frame
	je	RX_TYPE_SUBTYPE, TS_BEACON, frame_from_our_BSS
	SETBIT(BOBBIT, GLOBAL_FLAGS_REG3)
frame_from_our_BSS:
	je	RX_TYPE_SUBTYPE, TS_PROBE_REQ, send_frame_to_host
	jext	COND_TRUE, LABEL345
not_multicast_frame:
	jnext	COND_STA_MODE, check_frame_type
	jnext	0x62, check_frame_type
	CLEANBIT(BOBBIT, GLOBAL_FLAGS_REG3)
check_frame_type:
	jne	RX_TYPE, T_DATA, not_data_frame_and_ra_doesnt_match
	add	[0x08F], 0x001, [0x08F]
	jext	COND_TRUE, data_frame_and_ra_doesnt_match
could_be_multicast_frame:
	je	RX_TYPE, T_DATA, data_frame_and_ra_doesnt_match
	jnzxh	[RX_FRAME_ADDR3_1,off1] & 1, send_frame_to_host
not_data_frame_and_ra_doesnt_match:
	jzxh	SPR_MAC_CTLHI & MAC_CTL_BEACON_PROMISC, data_frame_and_ra_doesnt_match
	je	RX_TYPE_SUBTYPE, TS_BEACON, send_frame_to_host
	je	RX_TYPE_SUBTYPE, TS_PROBE_RESP, send_frame_to_host
data_frame_and_ra_doesnt_match:
#ifdef ENABLE_PROMISC
	jzxh	SPR_MAC_CTLHI & MAC_CTL_PROMISCUOUS, discard_frame
	jext	COND_TRUE, send_frame_to_host
#else
	jext	COND_TRUE, discard_frame
#endif // ENABLE_PROMISC
rx_control_frame:
	jnext	COND_RX_RAMATCH, send_frame_to_host
	je	RX_TYPE_SUBTYPE, TS_RTS, LABEL345
	je	RX_TYPE_SUBTYPE, TS_PSPOLL, LABEL345
	jext	COND_TRUE, send_frame_to_host
rx_frame_and_ra_match:
not_wds_frame:
	jnext	COND_FRAME_NEED_ACK, LABEL343
	srxh	([TXHDR_FCTL,off0] >> 2) & 63, REG36
LABEL343:
	je	RX_TYPE_SUBTYPE, TS_ASSOC_REQ, send_frame_to_host
	je	RX_TYPE_SUBTYPE, TS_REASSOC_REQ, send_frame_to_host
	je	RX_TYPE_SUBTYPE, TS_AUTH, send_frame_to_host
LABEL345:
	mov	[RX_FRAME_ADDR2_1,off1], SPR_PMQ_pat_0
	mov	[RX_FRAME_ADDR2_2,off1], SPR_PMQ_pat_1
	mov	[RX_FRAME_ADDR2_3,off1], SPR_PMQ_pat_2
	srxh	([RX_FRAME_FC,off1] >> 12) & 1, REG34
	add	REG34, 0x001, SPR_PMQ_dat
	mov	[0x016],SPR_PMQ_control_low
	mov	SPR_PMQ_control_low, 0x000
	srxh	(SPR_PMQ_control_high >> 9) & 63, REG34
	jext	COND_TRUE, send_frame_to_host

// ***********************************************************************************************
// HANDLER:	send_frame_to_host
// PURPOSE:	Prepares the frame before sending it to the host.
//
send_frame_to_host:
#ifdef ENABLE_PROMISC
	jnzxh	SPR_MAC_CTLHI & MAC_CTL_KEEP_BADFRAMES, keep_bad_frames
#endif // ENABLE_PROMISC
	jnzxh	GLOBAL_FLAGS_REG3 & GFR3_DISCARD_FRAME, discard_frame
keep_bad_frames:
	mov	SPR_RXE_FRAMELEN, REG34
	mov	REG34, [SHM_RXHDR_FLEN]
	jzxh	SPR_RXE_FIFOCTL1 & 32, no_hdr_length_update
	add	REG34, [SHM_RXPADOFF], [SHM_RXHDR_FLEN]
	orxh	0x0004, [SHM_RXHDR_MACST_LOW] & ~0x0004, [SHM_RXHDR_MACST_LOW]
no_hdr_length_update:
	srxh	(GLOBAL_FLAGS_REG3 >> 4) & 1, REG34
	orxh	(REG34 << 15) & 0x8000, [SHM_RXHDR_MACST_LOW] & ~0x8000, [SHM_RXHDR_MACST_LOW]
wait_crypto_engine:
	jext	COND_RX_FIFOFULL, rx_fifo_overflow
	jext	COND_RX_CRYPTBUSY, wait_crypto_engine
	srxh	(SPR_WEP_CTL >> 15) & 1, REG34
	orxh	(REG34 << 4) & 0x0010, [SHM_RXHDR_MACST_LOW] & ~0x0010, [SHM_RXHDR_MACST_LOW]
	or	SPR_RXE_PHYRXSTAT0, 0x000, [SHM_RXHDR_PHYST0]
	or	SPR_RXE_PHYRXSTAT1, 0x000, [SHM_RXHDR_PHYST1]
	or	SPR_RXE_PHYRXSTAT2, 0x000, [SHM_RXHDR_PHYST2]
	or	SPR_RXE_PHYRXSTAT3, 0x000, [SHM_RXHDR_PHYST3]
	srxh	(SPR_RXE_PHYRXSTAT0 >> 5) & 1, [SHM_LAST_RX_ANTENNA]
	orx	7, 8, 0x0FF, 0x0FE, ANTENNA_DIVERSITY_CTR
	call	lr1, antenna_diversity_helper
	call	lr0, push_frame_into_fifo
	nand	SPR_RXE_FIFOCTL1, 0x002, SPR_RXE_FIFOCTL1
	jext	COND_TRUE, tx_contention_params_update

// ***********************************************************************************************
// HANDLER:	rx_too_long
// PURPOSE:	Reports reception error.	
//
rx_too_long:
	add	[0x082], 0x001, [0x082]
	orxh	TX_ERROR, SPR_BRC & ~ TX_ERROR, SPR_BRC
	orxh	RX_ERROR, SPR_BRC & ~ RX_ERROR, SPR_BRC
	jext	COND_TRUE, discard_frame

// ***********************************************************************************************
// HANDLER:	rx_ack
// PURPOSE:i	Performs operations related to ACK reception.	
//
rx_ack:
	jnext	COND_RX_RAMATCH, ack_not_for_us
	add	[0x08E], 0x001, [0x08E]
	jnext	COND_FRAME_NEED_ACK, send_control_frame_to_host
	jne	RX_TYPE_SUBTYPE, EXPECTED_CTL_RESPONSE, send_control_frame_to_host
	orxh	0x0000, SPR_TXE0_TIMEOUT & ~0x8000, SPR_TXE0_TIMEOUT
	orxh	0x000, SPR_BRC & ~ TX_ERROR, SPR_BRC
	or	REG34, 0x000, REG34
	jle	0x000, 0x001, flush_pipe
flush_pipe:
	extcond_eoi_only(COND_TX_PMQ)
	jext	COND_TRUE, send_control_frame_to_host
ack_not_for_us:
	jne	RX_TYPE_SUBTYPE, TS_CTS, send_control_frame_to_host
	add	[0x093], 0x001, [0x093]
	jext	COND_TRUE, send_control_frame_to_host

// ***********************************************************************************************
// HANDLER:	send_control_frame_to_host
// PURPOSE:	Decides if control frame must be sent to host.	
//
send_control_frame_to_host:
	jext	COND_RX_RAMATCH, send_control_frame_and_ra_match
#ifdef ENABLE_PROMISC
	jzxh	SPR_MAC_CTLHI & MAC_CTL_PROMISCUOUS, discard_frame
#else
	jext	COND_TRUE, rx_discard_frame
#endif // ENABLE_PROMISC
send_control_frame_and_ra_match:
	jnzxh	SPR_MAC_CTLHI & MAC_CTL_KEEP_CTL, rx_complete
	jext	COND_TRUE, rx_discard_frame

// ***********************************************************************************************
// HANDLER:	rx_check_promisc
// PURPOSE:	Controls if promiscuous mode was enable.	
//
rx_check_promisc:
	jnzxh	SPR_MAC_CTLHI & MAC_CTL_PROMISCUOUS, rx_complete

// ***********************************************************************************************
// HANDLER:	rx_discard_frame	
// PURPOSE:	Commands a frame discard.
//
rx_discard_frame:
	orxh	GFR3_DISCARD_FRAME, GLOBAL_FLAGS_REG3 & ~ GFR3_DISCARD_FRAME, GLOBAL_FLAGS_REG3
	jext	COND_TRUE, rx_complete

// ***********************************************************************************************
// HANDLER:	rx_data_plus
// PURPOSE:	Manages data frame reception.	
//
rx_data_plus:
	jext	COND_RX_COMPLETE, end_rx_data_plus
	jl	SPR_RXE_FRAMELEN, 0x01C, rx_data_plus
end_rx_data_plus:
	jl	SPR_RXE_FRAMELEN, 0x01C, rx_check_promisc
#ifdef ENABLE_RX_ALWAYS_IDLE
	jnext	COND_RX_RAMATCH, state_machine_idle
#else
	jnext	COND_RX_RAMATCH, rx_ra_dont_match
#endif // ENABLE_RX_ALWAYS_IDLE
	jext	COND_TRUE, send_response

// ***********************************************************************************************
// HANDLER:	tx_underflow	
// PURPOSE:	Prepares device for TX underflow error management.	
//
// XXX

// ***********************************************************************************************
// HANDLER:	tx_fifo_underflow
// PURPOSE:	Manages TX underflow error.	
//
// XXX

	// for my memory only larrybird linksys03 pescosolido execute the following
	// though the linksys is that it reveals executing the code after the jumps
tx_clear_issues:
	orx	7, 8, 0x000, 0x001, REG36

tx_dont_clear_issues:
	jnext	COND_FRAME_NEED_ACK, check_underflow_cond

	// for my memory only linksys as STA execute the following
	orxh	0x0000, SPR_BRC & ~ FRAME_NEED_ACK, SPR_BRC
	orx	7, 8, 0x000, 0x000, EXPECTED_CTL_RESPONSE
	orxh	0x0000, SPR_TXE0_TIMEOUT & ~0x8000, SPR_TXE0_TIMEOUT
	orxh	0x0000, SPR_BRC & ~ MORE_FRAGMENT, SPR_BRC
	call	lr1, set_backoff_time
check_underflow_cond:
	extcond_eoi_only(COND_TX_POWER)
	extcond_eoi_only(COND_TX_NOW)
	orxh	0x0000, SPR_BRC & ~ FRAME_BURST, SPR_BRC
	extcond_eoi_only(COND_TX_UNDERFLOW)
	orx	7, 8, 0x000, 0x000, SPR_TXE0_SELECT
	orx	7, 8, 0x000, 0x007, REG34
	je	[SHM_PHYTYPE], 0x000, end_tx_fifo_underflow
	orxh	(SPR_TXE0_PHY_CTL << 10) & 0x0400, REG34 & ~0x0400, REG34
end_tx_fifo_underflow:
	call	lr0, sel_phy_reg
	or	SPR_Ext_IHR_Data, 0x000, REG38
	orx	7, 8, 0x0FF, 0x0FF, REG35
	call	lr0, write_phy_reg
	xor	REG34, REG37, REG34
	call	lr0, write_phy_reg
	je	REG36, 0x000, state_machine_idle
	or	REG38, 0x000, [TXHDR_RTSPHYSTAT,off0]
	jext	COND_TRUE, suppress_this_frame

// ***********************************************************************************************
// HANDLER:	tx_phy_error
// PURPOSE:	Manages TX phy errors.
//
// XXX
tx_phy_error:
	jext	COND_TRUE, check_rx_conditions

// ***********************************************************************************************
// HANDLER:	rx_fifo_overflow
// PURPOSE:	Manages RX overflow error.	
//		Is the first instruction useful to clear some hardware exception? Can be safely removed?
//
// This code seems to be useful only on pccard
rx_fifo_overflow_pre:
	orxh	0x0000, SPR_BRC & ~ REC_IN_PROGRESS, SPR_BRC

rx_fifo_overflow:
overflow_frame_too_long:
	jext	COND_REC_IN_PROGRESS, rx_complete
	extcond_eoi_only(COND_RX_FIFOFULL)
	orxh	RX_ERROR, SPR_BRC & ~ RX_ERROR, SPR_BRC
	jext	COND_TRUE, discard_frame


// ***********************************************************************************************
// HANDLER:	mac_suspend_check	
// PURPOSE:	Checks if device can be suspended.
//		The condition on SPR_BRC involves
//		COND_NEED_RESPONSEFR|COND_FRAME_BURST|COND_REC_IN_PROGRESS|COND_FRAME_NEED_ACK
//
mac_suspend_check:
	jnand	(NEED_RESPONSEFR|FRAME_BURST|REC_IN_PROGRESS|FRAME_NEED_ACK), SPR_BRC, check_conditions
	jnzxh	SPR_IFS_STAT & 256, check_conditions
	jext	COND_TX_DONE, check_conditions
	jnzxh	SPR_IFS_STAT & 256, check_conditions
	jext	COND_TX_DONE, check_conditions
	jext	COND_TX_PHYERR, check_conditions
	call	lr0, flush_and_stop_tx_engine

// ***********************************************************************************************
// HANDLER:	mac_suspend	
// PURPOSE:	Suspends device.
//		
mac_suspend:
	orx	7, 8, 0x000, 0x001, SPR_MAC_IRQLO
	orxh	0x0000, SPR_TSF_GPT0_STAT & ~0x8000, SPR_TSF_GPT0_STAT
	orx	7, 8, 0x000, 0x003, [SHM_UCODESTAT]
	orx	7, 8, 0x003, 0x003, SPR_WEP_0x50
wait_for_mac_to_disable:
	jnext	COND_MACEN, wait_for_mac_to_disable
	orx	7, 8, 0x000, 0x002, [SHM_UCODESTAT]
	orx	7, 8, 0x003, 0x0B4, [0x05F]
	orx	7, 8, 0x003, 0x0B4, [0x05E]
	srxh	(SPR_MAC_CTLHI >> 15) & (MAC_CTL_GMODE >> 15), GLOBAL_FLAGS_REG1
	orx	7, 8, 0x003, 0x001, SPR_WEP_0x50
	orx	7, 8, 0x083, 0x000, SPR_WEP_CTL

	orx	7, 8, 0x000, 0x000, SPR_BRC
	nand	GLOBAL_FLAGS_REG2, 0x10|0x08|0x02, GLOBAL_FLAGS_REG2
	orx	7, 8, 0x0FF, 0x0FF, SPR_BRCL0
	orx	7, 8, 0x0FF, 0x0FF, SPR_BRCL1
	orx	7, 8, 0x0FF, 0x0FF, SPR_BRCL2
	orx	7, 8, 0x0FF, 0x0FF, SPR_BRCL3
	orxh	0x0004, SPR_RXE_FIFOCTL1 & ~0x0004, SPR_RXE_FIFOCTL1
wait_RXE_FIFOCTL1_cond_to_clear:
	jnzxh	SPR_RXE_FIFOCTL1 & 4, wait_RXE_FIFOCTL1_cond_to_clear
	orxh	0x8000, SPR_TSF_GPT0_STAT & ~0x8000, SPR_TSF_GPT0_STAT
	orx	7, 8, 0x000, 0x000, SPR_BRCL0
	orx	7, 8, 0x000, 0x000, SPR_BRCL1
	orx	7, 8, 0x000, 0x000, SPR_BRCL2
	orx	7, 8, 0x000, 0x000, SPR_BRCL3
	orx	7, 8, 0x003, 0x001, [0x017]
	srxh	(SPR_MAC_CTLHI >> 13) & 1, REG34
	orxh	(REG34 << 4) & 0x0010, [0x017] & ~0x0010, [0x017]
	srxh	(SPR_MAC_CTLHI >> 14) & 1, REG34
	xor	REG34, 0x001, REG34
	orxh	(REG34 << 1) & 0x0002, 0x000 & ~0x0002, [0x016]

	orx	7, 8, 0x073, 0x060, SPR_BRWK0
	orx	7, 8, 0x000, 0x000, SPR_BRWK1
	orx	7, 8, 0x073, 0x00F, SPR_BRWK2
	orx	7, 8, 0x000, 0x057, SPR_BRWK3
	jext	COND_TRUE, state_machine_start

// ***********************************************************************************************
// HANDLER:	rx_badplcp	
// PURPOSE:	Manages reception of a frame with not valid PLCP.
//
// Will set bit 0x0010 of GLOBAL_FLAGS_REG2
rx_badplcp:
	jnzxh	SPR_RXE_0x1a & 2048, state_machine_idle
	jnzxh	SPR_RXE_0x1a & 4096, rx_badplcp
	SETBIT(0x10, GLOBAL_FLAGS_REG2)
	add	[0x086], 0x001, [0x086]
	jext	COND_RX_FIFOFULL, rx_fifo_overflow
	jnzxh	SPR_RXE_0x1a & 32768, rx_fifo_overflow
update_RXE_FIFOCTL1_value:
	orx	7, 8, 0x000, 0x004, SPR_RXE_FIFOCTL1
	or	SPR_RXE_FIFOCTL1, 0x000, REG34
	jext	COND_TRUE, state_machine_start

// ***********************************************************************************************
// HANDLER:	discard_frame	
// PURPOSE:	Discards the frame into the FIFO.
//
// if calling flush_and_stop_tx_engine then set bit 0x1000 of GLOBAL_FLAGS_REG1
// NOTE interesting the SPR_RXE_FIFOCTL1 should be read even not assigned
// Will set bit 0x1000 of GLOBAL_FLAGS_REG1
discard_frame:
	orx	7, 8, 0x000, 0x014, SPR_RXE_FIFOCTL1
	or	SPR_RXE_FIFOCTL1, 0x000, 0x000
	srxh	(SPR_WEP_CTL >> 5) & 7, REG34
	jnext	COND_RX_ERROR, tx_contention_params_update
	orxh	0x1000, GLOBAL_FLAGS_REG1 & ~0x1000, GLOBAL_FLAGS_REG1
	call	lr0, flush_and_stop_tx_engine
	orxh	0x0001, SPR_TXE0_AUX & ~0x0001, SPR_TXE0_AUX
	or	REG34, 0x000, REG34
	orxh	0x0000, SPR_TXE0_AUX & ~0x0001, SPR_TXE0_AUX
	jext	COND_TRUE, tx_contention_params_update

// ***********************************************************************************************
// HANDLER:	flush_and_stop_tx_engine	
// PURPOSE:	Checks if there are any other frames into the queue, flushes the TX engine and stops it.
//
// With respect to 5.2 the WEP conditional jump was removed (I'm removing WEP support).
// Currently I switch back to Broadcom style for going back to caller (but it "sucks")
//
// May clear both bits 0x2000 | 0x1000 of GLOBAL_FLAGS_REG1
flush_and_stop_tx_engine:
	orx	7, 8, 0x040, 0x000, SPR_TXE0_CTL
	or	SPR_TXE0_CTL, 0x000, 0x000
	jle	0x000, 0x001, check_pending_tx_and_stop
check_pending_tx_and_stop:
	jnext	EOI(COND_TX_NOW), pending_tx_resolved
	// not all device jump above:
	// for my memory only the following devices may jump to tx_frame_now
	// AP = [aspirino_ap larrybird_ap linksys03_ap]
	// STA = [larrybird linksys03 pescosolido]
	jext	COND_TRUE, tx_frame_now
pending_tx_resolved:
	nand	SPR_BRC, (FRAME_BURST|NEED_BEACON|NEED_RESPONSEFR|NEED_PROBE_RESP), SPR_BRC
	orx	7, 8, 0x000, 0x000, SPR_TXE0_SELECT
	orxh	0x0000, SPR_TXE0_TIMEOUT & ~0x8000, SPR_TXE0_TIMEOUT
	orxh	0x0000, SPR_BRC & ~ MORE_FRAGMENT, SPR_BRC
	orxh	0x0000, GLOBAL_FLAGS_REG1 & ~0x3000, GLOBAL_FLAGS_REG1
	ret	lr0, lr0

// ***********************************************************************************************
// HANDLER:	rx_beacon_probe_resp	
// PURPOSE:	Analyzes Beacon or Probe Response frame that has been received. Important for time synchronization.
//		off3 is a pointer that has been load before by get_ptr_from_rate_table with a value coming
//		from the second level rate tables, e.g., on a beacon in 2.4MHz off3 = 0x37E
//
// Question: who is setting SHM_TBL_OFF2DUR? SHM(0x038) /* Offset to duration in second level rate tables */
// Maybe initvals. TBC
// NOTE: a lot of stuff was removed with respect to 5.2.
// NOTE: bit 0x0040 of GLOBAL_FLAGS_REG3 tells if the last received beacon was carrying a DTIM saying there is multicast or broadcast
//       traffic in the AP queue (not sure)
rx_beacon_probe_resp:
	jl	SPR_RXE_FRAMELEN, 0x02C, rx_discard_frame

	// STA may jump here, AP NEVER!
	jext	COND_RX_BSSMATCH, rx_bss_match

	// STA and AP can get here
	jext	COND_TRUE, no_time_informations

rx_bss_match:
	// from here on only STA
	je	RX_TYPE_SUBTYPE, TS_PROBE_RESP, check_beacon_time
	jext	COND_AP_MODE, rx_beacon_probe_resp_end

check_beacon_time:
	jext	COND_AP_MODE, rx_beacon_probe_resp_end
	mov	[SHM_TBL_OFF2DUR], REG34
	add	REG34, [0x00,off3], REG34
	add.	LAST_RX_TIME_WORD0, REG34, LAST_RX_TIME_WORD0
	addc.	LAST_RX_TIME_WORD1, 0x000, LAST_RX_TIME_WORD1
	addc.	LAST_RX_TIME_WORD2, 0x000, LAST_RX_TIME_WORD2
	addc	LAST_RX_TIME_WORD3, 0x000, LAST_RX_TIME_WORD3

	// an old jump from 5.2: but in STA mode it always jump, the old code
	// was removed
	// jext	COND_STA_MODE, sync_TSF
	// REMOVED

sync_TSF:
	or	SPR_TSF_WORD0, 0x000, [SHM_RX_TIME_WORD0]
	or	SPR_TSF_WORD1, 0x000, [SHM_RX_TIME_WORD1]
	or	SPR_TSF_WORD2, 0x000, [SHM_RX_TIME_WORD2]
	or	SPR_TSF_WORD3, 0x000, [SHM_RX_TIME_WORD3]
	jne	[SHM_RX_TIME_WORD0], SPR_TSF_WORD0, sync_TSF
	sub.	[SHM_RX_TIME_WORD0], LAST_RX_TIME_WORD0, LAST_RX_TIME_WORD0
	subc.	[SHM_RX_TIME_WORD1], LAST_RX_TIME_WORD1, LAST_RX_TIME_WORD1
	subc.	[SHM_RX_TIME_WORD2], LAST_RX_TIME_WORD2, LAST_RX_TIME_WORD2
	subc	[SHM_RX_TIME_WORD3], LAST_RX_TIME_WORD3, LAST_RX_TIME_WORD3
update_TSF_words:
	add.	LAST_RX_TIME_WORD0, [RX_FRAME_BCN_TIMESTAMP_0,off1], REG34
	or	REG34, 0x000, SPR_TSF_WORD0
	addc.	LAST_RX_TIME_WORD1, [RX_FRAME_BCN_TIMESTAMP_1,off1], SPR_TSF_WORD1
	addc.	LAST_RX_TIME_WORD2, [RX_FRAME_BCN_TIMESTAMP_2,off1], SPR_TSF_WORD2
	// in 5.2 we are using addc. instead of addc here below
	addc	LAST_RX_TIME_WORD3, [RX_FRAME_BCN_TIMESTAMP_3,off1], SPR_TSF_WORD3
	jne	REG34, SPR_TSF_WORD0, update_TSF_words
	jnext	COND_STA_MODE, rx_beacon_probe_resp_end

no_time_informations:

	// ap can get here: we should check CF (contention free) info if interested in this point
	je	RX_TYPE_SUBTYPE, TS_PROBE_RESP, rx_beacon_probe_resp_end

	// ZZZ 0xA32 in SPR_BASE5, andrebbe ricodificato come SPR_BASE1 + SHM_OFFSET(0x2A)
	mov	SHM_BEACON_DATA, SPR_BASE5
	jnext	COND_STA_MODE, rx_beacon_probe_resp_end
	jext	COND_AP_MODE, rx_beacon_probe_resp_end

	// following code not executed on AP
	je	RX_TYPE_SUBTYPE, TS_PROBE_RESP, rx_beacon_probe_resp_end
	jnext	COND_RX_BSSMATCH, rx_beacon_probe_resp_end
	// find TIM data in beacon (tag number 5)
	orx	7, 8, 0x000, 0x005, REG37
	call	lr0, find_beacon_info_elem
	// not found!
	jne	REG37, 0x005, rx_beacon_probe_resp_end
	jzxh	SPR_BASE5 & 32768, load_tim_from_even_addr
	srxh	([0x01,off5] >> 8) & 255, CURRENT_DTIM_COUNTER
	srxh	([0x02,off5] >> 8) & 255, REG34
	jext    COND_TRUE, tim_loaded
load_tim_from_even_addr:
	srxh	[0x01,off5] & 255, CURRENT_DTIM_COUNTER
	srxh	[0x02,off5] & 255, REG34
tim_loaded:
	// I'm not sure here TBC
	// CURRENT_DTIM_COUNTER should be the DTIM_COUNTER
	// REG34 should be the Bitmap Control whose lsb set to 1 tells that
	// there is broadcast or multicast traffic for some station
	// Remember in bit 0x0040 of GLOBAL_FLAGS_REG3 and copy its value
	// in bit 0x8000 of SPR_TSF_GPT1_STAT (this should avoid sleeping
	// like we do for TBTT)
	orxh	(REG34 << 6) & 0x0040, GLOBAL_FLAGS_REG3 & ~0x0040, GLOBAL_FLAGS_REG3
	orxh	(REG34 << 15) & 0x8000, SPR_TSF_GPT1_STAT & ~0x8000, SPR_TSF_GPT1_STAT
rx_beacon_probe_resp_end:
	jext	COND_RX_RAMATCH, send_response
	jext	COND_TRUE, rx_complete

// ***********************************************************************************************
// HANDLER:	send_response_if_ra_match
// PURPOSE:	Decides if frame needs a response.
//
send_response_if_ra_match:
	jext	COND_RX_RAMATCH, send_response
rx_ra_dont_match:
	jzxh	[RX_FRAME_ADDR1_1,off1] & 1, rx_check_promisc
	jext	COND_TRUE, rx_complete

// ***********************************************************************************************
// HANDLER:	slow_clock_control
// PURPOSE:	Updates SCC.
//
// This operation is skipped if
// 1) bit 0x0004 of GLOBAL_FLAGS_REG3 is not zero
// 2) bit 0x0002 of SPR_SCC_Control is not zero
// 3) something is being handled by the state machine (jnand on SPR_BRC)
// When executed, set bit 0x0004 of GLOBAL_FLAGS_REG3 to 1 (0x0004)
// so that the operation is not repeated until the same bit is cleared by someone else.
// Unfortunately it seems that no one will ever clear this bit!!
// Does this mean that we perform SCC just once?
slow_clock_control:
	// this seems to be useless since we clear bit 0x8000 that is initially zero and never set to 1 (0x8000)
	//orx	0, 15, 0x000, GLOBAL_FLAGS_REG1, GLOBAL_FLAGS_REG1
	jnand	NEED_BEACON|NEED_RESPONSEFR|NEED_PROBE_RESP|CONTENTION_PARAM_MODIFIED|MORE_FRAGMENT|FRAME_BURST|REC_IN_PROGRESS|FRAME_NEED_ACK, SPR_BRC, state_machine_idle
	jnzxh	GLOBAL_FLAGS_REG3 & 4, skip_scc_update
	jnzxh	SPR_SCC_Control & 2, state_machine_idle
	orxh	(SPR_SCC_Timer_Low << 1) & 0xFFFE, 0x000 & ~0xFFFE, SPR_SCC_Period_Divisor
	srxh	(SPR_SCC_Timer_Low >> 15) & 1, REG34
	orxh	(SPR_SCC_Timer_High << 1) & 0xFFFE, REG34 & ~0xFFFE, SPR_SCC_Period
	orxh	0x0004, GLOBAL_FLAGS_REG3 & ~0x0004, GLOBAL_FLAGS_REG3
skip_scc_update:
	jext	COND_TRUE, state_machine_idle

/* --------------------------------------------------- FUNCTIONS ---------------------------------------------------------- */


// ***********************************************************************************************
// FUNCTION:	push_frame_into_fifo
// PURPOSE:	Copies received frame into the RX host queue.
//
// Tells the host that a new packet is available at RX raising a IRQ on IRQLO
push_frame_into_fifo:
	mov	SHM_RXHDR, SPR_RXE_RXHDR_OFFSET
	mov	SHM_RXHDR_LEN, SPR_RXE_RXHDR_LEN
	orxh	0x0001, SPR_RXE_FIFOCTL1 & ~0x0003, SPR_RXE_FIFOCTL1
wait_rx_fifo_1:
	jext	COND_RX_FIFOFULL, rx_fifo_overflow
	jnext	COND_RX_FIFOBUSY, wait_rx_fifo_1
wait_rx_fifo_2:
	jext	COND_RX_FIFOFULL, rx_fifo_overflow
	jext	COND_RX_FIFOBUSY, wait_rx_fifo_2
	or	REG34, 0x000, REG34
	jle	0x000, 0x001, check_rx_fifo_overflow
check_rx_fifo_overflow:
	jext	COND_RX_FIFOFULL, rx_fifo_overflow
	orx	7, 8, 0x001, 0x000, SPR_MAC_IRQLO
	ret	lr0, lr0

// ***********************************************************************************************
// FUNCTION:	load_tx_header_into_shm
// PURPOSE:	Loads BCM header into SHM.
//
// Since we are fetching packets from one queue only we can assign
// SPR_BASE0 immediately.
// NOTE: header is copied actually only if bit 0x0002 of TXHDR_HK4 is zero
// After the copy it is initialized to 1 (TXHDR_HK4 |= 0x0002)
// so that calling this function again does not overwrite the header
// and the temporary information stored during the access attempt.
// The bit will be cleared by report_tx_status_to_host at the end
// of the current transmission.
load_tx_header_into_shm:
	mov	SHM_TXHEADER, SPR_BASE0
	mov	0x0000, REG34
	jnzxh	[TXHDR_HK4,off0] & 2, load_tx_hdr_done
	orxh	0x4000, [SHM_TXFCUR] & ~0x4000, SPR_TXE0_FIFO_CMD
	sl	SPR_BASE0, 0x001, SPR_TXE0_TX_SHM_ADDR
	or	[SHM_TXFCUR], 0x000, SPR_TXE0_SELECT
	mov	TXHDR_LEN, SPR_TXE0_TX_COUNT
	or	[SHM_TXFCUR], 0x005, SPR_TXE0_SELECT
load_hdr_wait_for_tx_engine:
	jnext	COND_TX_BUSY, load_hdr_wait_for_tx_engine
load_hdr_wait_for_tx_engine_again:
	jext	COND_TX_BUSY, load_hdr_wait_for_tx_engine_again
	orxh	0x0002, [TXHDR_HK4,off0] & ~0x0003, [TXHDR_HK4,off0]
	jzxh	[TXHDR_MACLO,off0] & 8, load_tx_hdr_done
	nand	[TXHDR_HK5,off0], 0x018, [TXHDR_HK5,off0]
load_tx_hdr_done:
	ret	lr3, lr3

// ***********************************************************************************************
// FUNCTION:	inhibit_sleep_at_tbtt
// PURPOSE:	Forces device to not sleep at TBTT. If DTIM counter goes zero
//              reset it back.
//
// Execute only on STA, never on AP
// Question: who initialize SHM_NOSLPZNATDTIM? SHM(0x04C)
inhibit_sleep_at_tbtt:
	orx	7, 8, 0x000, 0x004, SPR_MAC_IRQLO
	sub	CURRENT_DTIM_COUNTER, 0x001, CURRENT_DTIM_COUNTER
	jges	CURRENT_DTIM_COUNTER, 0x000, LABEL53
	sub	[SHM_DTIMPER], 0x001, CURRENT_DTIM_COUNTER
LABEL53:
	extcond_eoi_only(COND_TX_TBTTEXPIRE)
	sl	[SHM_NOSLPZNATDTIM], 0x003, SPR_TSF_GPT1_CNTLO
	sr	[SHM_NOSLPZNATDTIM], 0x00D, SPR_TSF_GPT1_CNTHI
	MOV(TIMER_RUNNING_8MHZ, SPR_TSF_GPT1_STAT)
	ret	lr0, lr0

// ***********************************************************************************************
// FUNCTION:	sel_phy_reg
// PURPOSE:	Selects phy register in REG34 for reading
//
sel_phy_reg:
	jnzxh	SPR_Ext_IHR_Address & IHR_BUSY, sel_phy_reg
	SETBIT_MOV(IHR_READ, REG34, SPR_Ext_IHR_Address)

wait_sel_phy_cond_to_clear:
	jnzxh	SPR_Ext_IHR_Address & IHR_READ, wait_sel_phy_cond_to_clear

	mov	REG34, REG34
	ret	lr0, lr0

// ***********************************************************************************************
// FUNCTION:	write_phy_reg
// PURPOSE:	Writes the value contained in REG35 into phy register in REG34
//
write_phy_reg:
	jnzxh	SPR_Ext_IHR_Address & IHR_BUSY, write_phy_reg
	mov	REG35, SPR_Ext_IHR_Data
	SETBIT_MOV(IHR_WRITE, REG34, SPR_Ext_IHR_Address)
	jnzxh	GLOBAL_FLAGS_REG1 & 0x8, end_write_phy_reg

wait_write_phy_cond_to_clear:
	jnzxh	SPR_Ext_IHR_Address & IHR_WRITE, wait_write_phy_cond_to_clear

end_write_phy_reg:
	mov	REG34, REG34
	ret	lr0, lr0

// ***********************************************************************************************
// FUNCTION:	get_ptr_from_rate_table
// PURPOSE:	Makes pointer refers to the correct preamble informations.
//		It takes the rate in GP_REG0 and the control in GP_REG1
//		rate values (from the b43 driver, xmit.c)
//
//		cck  at [1, 2, 5, 11] => [ 0x0A, 0x14, 0x37, 0x6E ]
//		ofdm at [6, 9, 12, 18, 24, 36, 48, 54] => [0xB, 0xF, 0xA, 0xE, 0x9, 0xD, 0x8, 0xC]
//
//		e.g. on reception of a beacon we have gp_reg0 = 0x0A and gp_reg1 = 0x00
//
get_ptr_from_rate_table:
	orx	7, 8, 0x000, 0x014, [SHM_PREAMBLE_DURATION]
	orxh	0x0000, REG0 & ~0xFFF0, REG0
	je	[SHM_PHYTYPE], 0x000, get_ptr_from_rate_table_ofdm
	jzxh	REG1 & 3, get_ptr_from_rate_table_cck
get_ptr_from_rate_table_ofdm:
	orx	7, 8, 0x000, 0x0F0, REG34
	add	REG0, REG34, SPR_BASE5
	orx	7, 8, 0x000, 0x0E0, REG34
	add	REG0, REG34, SPR_BASE4
	orx	7, 8, 0x000, 0x001, [SHM_CURMOD]
	jext	COND_TRUE, get_ptr_from_rate_table_out
get_ptr_from_rate_table_cck:
	orx	7, 8, 0x001, 0x010, REG34
	add	REG0, REG34, SPR_BASE5
	orx	7, 8, 0x001, 0x000, REG34
	add	REG0, REG34, SPR_BASE4
	orx	7, 8, 0x000, 0x0C0, [SHM_PREAMBLE_DURATION]
	orx	7, 8, 0x000, 0x000, [SHM_CURMOD]
get_ptr_from_rate_table_out:
	or	[0x00,off5], 0x000, SPR_BASE2
	or	[0x00,off4], 0x000, SPR_BASE3
	ret	lr1, lr1

// ***********************************************************************************************
// FUNCTION:	find_beacon_info_elem
// PURPOSE:	Extracts TAG informations from Beacon frame.
//
// First determine the end of the received beacon
// (depends on the frame length and how much of the packet is buffered in shm)
// Then loop using SPR_BASE5 (initially it points to byte 36 after the first byte
// of the beacon payload, not plcp: that is 24(MAC) + 12(TS) = 36(beginning of
// tagged parameters)
// REG37: first time is 4, then retry with 5
// Attention: SPR_BASE5 may have bit 0x8000 as results of consecutive rr ops.
// In that case it points to an odd address (very strange!) hence
// the check before extract REG34 (type) and REG35 (length of type).
// When an element whose type is equal to the one passed in REG37
// then set R34 with the address of next element and if the next
// is within the received buffered beacon leave REG37 unchanged.
// In all other cases set REG37 = -1 (0xffff).
// NOTE: RR is rotate right, lsb re-enters on the left
//
find_beacon_info_elem:
	sub	SPR_RXE_FRAMELEN, 0x004, REG34
	or	SPR_RXE_Copy_Length, 0x000, REG36
	jl	REG34, REG36, align_offset_1
	sr	REG36, 0x001, REG36
	jext	COND_TRUE, align_offset_2
align_offset_1:
	sr	REG34, 0x001, REG36
align_offset_2:
	add	REG36, SPR_RXE_Copy_Offset, REG36
loop_inside_beacon_infos:
	// REG36 end of data
	// REG34 current pointer from SPR_BASE5, when REG34 > REG36 exit
	orxh	(SPR_BASE5 << 0) & 0x7FFF, 0x000 & ~0x7FFF, REG34
	jge	REG34, REG36, update_return_value
	jnzxh	SPR_BASE5 & 32768, extract_beacon_informations
	srxh	[0x00,off5] & 255, REG34
	srxh	([0x00,off5] >> 8) & 255, REG35
	jext	COND_TRUE, compute_oper_on_infos
extract_beacon_informations:
	srxh	([0x00,off5] >> 8) & 255, REG34
	srxh	[0x01,off5] & 255, REG35
compute_oper_on_infos:
	jge	REG34, REG37, finish_operations_on_beacon
	rr	REG35, 0x001, REG35
	add.	SPR_BASE5, REG35, SPR_BASE5
	addc.	SPR_BASE5, 0x001, SPR_BASE5
	jext	COND_TRUE, loop_inside_beacon_infos
finish_operations_on_beacon:
	jne	REG34, REG37, update_return_value
	// never seen an AP executing the following code
	rr	REG35, 0x001, REG35
	add.	SPR_BASE5, REG35, REG34
	addc.	REG34, 0x001, REG34
	orxh	(REG34 << 0) & 0x7FFF, 0x000 & ~0x7FFF, REG34
	// it seems to always jump, however we left conditional jump
	jle	REG34, REG36, end_find_beacon_info_elem
update_return_value:
	mov	0xFFFF, REG37
end_find_beacon_info_elem:
	ret	lr0, lr0

// ***********************************************************************************************
// FUNCTION:	prep_phy_txctl_with_encoding	
// PURPOSE:	Sets PHY parameters correctly according to the transmission needs.
//
// No POWER CONTROL here. We should add
//	1) check if power control is in use, bit 0x0200 of SPR_TXE0_PHY_CTL
//	2) refresh SHM_LAST_RX_ANTENNA in bit 0x0300 of SPR_TXE0_PHY_CTL
//	3) check if power control is requested by user, bit 0x0080 of SHM_HF_MI
//	4) refresh bits 0xFC00 of SPR_TXE0_PHY_CTL with (values in SHM_TXPWRCUR summed with [0x07,off5]) shifted left 10 times
//
// NOTE the second code entry is useless since we do not handle power control but we leave it here as future entry
prep_phy_txctl_with_encoding:
	orxh	(REG1 << 0) & 0x0003, SPR_TXE0_PHY_CTL & ~0x0003, SPR_TXE0_PHY_CTL
prep_phy_txctl_encoding_already_set:
	ret	lr1, lr1

// ***********************************************************************************************
// FUNCTION:	get_rate_table_duration
// PURPOSE:	Provides duration parameter.
//		If short preamble is requested, then subracts half of the preamble duration
//		to overall duration
//
get_rate_table_duration:
	or	[0x04,off2], 0x000, REG34
	jzxh	REG1 & 16, end_get_rate_table_duration

	// not executed on linksys in AP mode
	jnzxh	REG1 & 1, end_get_rate_table_duration

	// not executed on linksys in AP mode
	sr	[SHM_PREAMBLE_DURATION], 0x001, REG35
	sub	[0x04,off2], REG35, REG34
end_get_rate_table_duration:
	ret	lr0, lr0

// ***********************************************************************************************
// FUNCTION:	antenna_diversity_helper
// PURPOSE:	Manages antenna diversity operations.
//
// Bit 0x0001 of GLOBAL_FLAGS_REG1 is used (copy the G mode of SPR_MAC_CTLHI, msb)
antenna_diversity_helper:
	jzxh	[SHM_HF_LO] & 1, end_antenna_diversity_helper
	add	ANTENNA_DIVERSITY_CTR, 0x001, ANTENNA_DIVERSITY_CTR
	jl	ANTENNA_DIVERSITY_CTR, [SHM_ANTSWAP], end_antenna_diversity_helper
	orx	7, 8, 0x000, 0x001, REG34
	je	[SHM_PHYTYPE], 0x001, B_phy
	orxh	(GLOBAL_FLAGS_REG1 << 10) & 0x0400, 0x02B & ~0x0400, REG34
B_phy:
	call	lr0, sel_phy_reg
	jne	ANTENNA_DIVERSITY_CTR, 0xFFFF, no_antenna_update
	orxh	([SHM_LAST_RX_ANTENNA] << 7) & 0x0080, SPR_Ext_IHR_Data & ~0x0080, REG35
	je	[SHM_PHYTYPE], 0x001, B_phy_2
	orxh	([SHM_LAST_RX_ANTENNA] << 8) & 0x0100, SPR_Ext_IHR_Data & ~0x0100, REG35
	jext	COND_TRUE, B_phy_2

	// not executed on pccard in STA mode
no_antenna_update:
	xor	SPR_Ext_IHR_Data, 0x080, REG35
	je	[SHM_PHYTYPE], 0x001, B_phy_2

	// not executed on pccard in STA mode
	xor	SPR_Ext_IHR_Data, 0x100, REG35
B_phy_2:
	call	lr0, write_phy_reg
	orx	7, 8, 0x000, 0x000, ANTENNA_DIVERSITY_CTR
end_antenna_diversity_helper:
	ret	lr1, lr1

// ***********************************************************************************************
// FUNCTION:	gphy_classify_control_with_arg
// PURPOSE:	Manages classify control for G PHY devices.
//
gphy_classify_control_with_arg:
	jne	[SHM_PHYTYPE], 0x002, end_gphy_classify_control_with_arg
	orx	7, 8, 0x008, 0x002, REG34
	call	lr0, write_phy_reg
end_gphy_classify_control_with_arg:
	ret	lr1, lr1

// ***********************************************************************************************
// FUNCTION:	check_gphy_sym_war	
// PURPOSE:	Checks for workaround.
//
check_gphy_sym_war:
	jzxh	[SHM_HF_LO] & 2, end_check_gphy_sym_war
	je	[SHM_PHYTYPE], 0x000, end_check_gphy_sym_war
	jnzxh	REG23 & 3, end_check_gphy_sym_war
	jne	RX_TYPE, 0x001, end_check_gphy_sym_war
	srxh	[RX_FRAME_PLCP_0,off1] & 255, REG34
	jle	REG34, 0x014, end_check_gphy_sym_war
	jne	[RX_FRAME_PLCP_1,off1], 0x050, end_check_gphy_sym_war
	// only on old debian STA (same kernel as others) and only when STA
	// maybe the board?
	orx	7, 8, 0x000, 0x001, GPHY_SYM_WAR_FLAG
	orxh	0x0010, SPR_IFS_CTL & ~0x0010, SPR_IFS_CTL
end_check_gphy_sym_war:
	ret	lr1, lr1

// ***********************************************************************************************
// FUNCTION:	bg_noise_sample	
// PURPOSE:	Performs a noise measurement on the channel.
//
// NOTE: use SPR_BASE5 to read from SHM(0x0088)
//
// Bit 0x0008 of GLOBAL_FLAGS_REG3 => 0 no measurement was started, start and set it to 1 (0x0008)
// When done, reset it back to zero.
// No one else changes this bit.
// Bit 0x0001 of GLOBAL_FLAGS_REG1 is used (copy the G mode of SPR_MAC_CTLHI, msb)
bg_noise_sample:
	jzxh	SPR_MAC_CMD & MAC_CMD_BGNOISE, stop_bg_noise_sample
	jnzxh	GLOBAL_FLAGS_REG3 & GFR3_MEASURING_NOISE, bg_noise_inprogress
	SETBIT(GFR3_MEASURING_NOISE, GLOBAL_FLAGS_REG3)
	mov	SPR_TSF_WORD0, 0
	mov	SPR_TSF_WORD1, [SHM_BGN_START_TSF1]
bg_noise_inprogress:
	mov	SPR_TSF_WORD0, 0
	sub	SPR_TSF_WORD1, [SHM_BGN_START_TSF1], REG37
	MOV(PHY_CURRENT_CHAN, REG34)
	call	lr0, sel_phy_reg
	srxh	SPR_Ext_IHR_Data & JSSIAUX_CHAN_MASK, [SHM_JSSIAUX]
	orxh	(GLOBAL_FLAGS_REG1 << PHY_ROUTING_BASEBIT) & (GFR1_G_MODE << PHY_ROUTING_BASEBIT), PHY_RX_STATUS, REG34
	call	lr0, sel_phy_reg
	orxh	(SPR_Ext_IHR_Data << 8) & JSSIAUX_STATUS_MASK, [SHM_JSSIAUX] & JSSIAUX_CHAN_MASK, [SHM_JSSIAUX]

	MOV(PHY_JSSI_NOISE_LO, REG34)
	mov	SHM_JSSI0, SPR_BASE5

	MOV(0x00, REG35)
loop_on_JSSI:
	add	REG35, 0x001, REG35
	add	SPR_TSF_WORD0, 0x002, REG36

wait_for_time_to_be_elapsed_2us:
	jext	COND_TX_NOW, stop_bg_noise_sample
	jzxh	SPR_IFS_STAT & IFS_STAT_RX_SIGDETEC, no_frame_to_transmit
	jl	REG37, 0x002, stop_bg_noise_sample
no_frame_to_transmit:
	jne	REG36, SPR_TSF_WORD0, wait_for_time_to_be_elapsed_2us
	call	lr0, sel_phy_reg

	orxh	(SPR_Ext_IHR_Data << 0) & 0x01FF, [0x00,off5] & ~0x01FF, [0x00,off5]
	jne	[SHM_PHYTYPE], 0x000, not_A_phy

	jnzxh	SPR_Ext_IHR_Data & 256, rise_bg_noise_complete_irq
	jext	COND_TRUE, A_phy
not_A_phy:
	rr	[0x00,off5], 0x008, [0x00,off5]
	xor	SPR_BASE5, 0x001, SPR_BASE5
A_phy:
	jl	REG35, 0x004, loop_on_JSSI
	jge	REG37, 0x002, rise_bg_noise_complete_irq

	add	SPR_TSF_WORD0, 24, REG36
wait_for_time_to_be_elapsed_24us:
	jext	COND_TX_NOW, stop_bg_noise_sample
	jnzxh	SPR_IFS_STAT & IFS_STAT_RX_SIGDETEC, stop_bg_noise_sample
	jne	REG36, SPR_TSF_WORD0, wait_for_time_to_be_elapsed_24us

rise_bg_noise_complete_irq:
	MOV(MAC_CMD_BGNOISE, SPR_MAC_CMD)
	MOV(MAC_IRQHI_NOISE_SAMPLE_READY, SPR_MAC_IRQHI)
	CLEANBIT(GFR3_MEASURING_NOISE, GLOBAL_FLAGS_REG3)
stop_bg_noise_sample:
	ret	lr3, lr2

// ***********************************************************************************************
// FUNCTION:	set_backoff_time
// PURPOSE:	Updates backoff time for contention operation.
//
set_backoff_time:
	and	SPR_TSF_Random, CUR_CONTENTION_WIN, SPR_IFS_BKOFFDELAY
	ret	lr1, lr1

// ***********************************************************************************************
// FUNCTION:	???
// PURPOSE:	???
//
// XXX
LABEL559:
	jnzxh	SPR_IFS_STAT & IFS_STAT_TXING, skip_on_ap
	jzxh	[SHM_HF_LO] & HF_ACPR, skip_on_ap

	// execute on STA (not AP)
	call	lr2, LABEL588

skip_on_ap:
	mov	REG34, REG34
	ret	lr3, lr3

// ***********************************************************************************************
// FUNCTION:	???
// PURPOSE:	first load 0x51 in PHY register 0xB, then load 0 or 4 in PHY register 0xD
//		(4 if something is scheduled to be transmitted in the future)
//		(0 if nothing has been scheduled)
//		If something is being received when called, then skip PHY settings and
//		set bit 0x40 in GLOBAL_FLAGS_REG2, otherwise do stuff and clean bit 0x40.
//		PHY settings avoided if radio is locked.
//
// XXX
LABEL588:
	jzxh	SPR_IFS_STAT & IFS_STAT_RXING, not_receiving
	SETBIT(0x40, GLOBAL_FLAGS_REG2)
	jext	COND_TRUE, dont_set_phy
not_receiving:
	CLEANBIT(0x40, GLOBAL_FLAGS_REG2)
	jnzxh	SPR_TXE0_PHY_CTL & TXE0_SCHEDULE_WORKING, tx_scheduled
	MOV(0, REG1)
	jext	COND_TRUE, no_tx_scheduled
tx_scheduled:
	MOV(4, REG1)
no_tx_scheduled:
	MOV(0x51, REG0)
	jnzxh	SPR_MAC_CTLHI & MAC_CTL_RADIOLOCK, dont_set_phy
	MOV(0xB, REG34)
	SETBIT(0x08, GLOBAL_FLAGS_REG1)
	and	REG0, 0x0FF, REG35
	call	lr0, write_phy_reg
	MOV(0x0D, REG34)
	mov	REG1, REG35
	call	lr0, write_phy_reg
	CLEANBIT(0x08, GLOBAL_FLAGS_REG1)
dont_set_phy:
	ret	lr2, lr2

#include "initvals.asm"

