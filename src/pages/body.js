import * as React from 'react';
import PropTypes from 'prop-types';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Toolbar from '@mui/material/Toolbar';

import teaser from '../static/teaser.png';
import georgia_logo from '../static/georgia-tech-logo.svg';
import sfu_logo from '../static/sfu-logo.svg';
import stanford_logo from '../static/stanford-cardinal-logo.svg';
import meta_logo from '../static/meta-logo.svg';

function Header(props) {
    const { sx, ...other } = props;
    return (
        <Box
            sx={{
                bgcolor: (theme) => (theme.palette.mode === 'dark' ? '#101010' : '#fff'),
                color: (theme) => (theme.palette.mode === 'dark' ? 'grey.300' : 'grey.800'),
                border: 'none',
                p: 0,
                my: 4,
                borderRadius: 2,
                fontSize: '1.7rem',
                fontWeight: 'bold',
                ...sx,
            }}
            {...other}
        />
    );
}

Header.propTypes = {
    /**
     * The system prop that allows defining system overrides as well as additional CSS styles.
     */
    sx: PropTypes.oneOfType([
        PropTypes.arrayOf(
            PropTypes.oneOfType([PropTypes.func, PropTypes.object, PropTypes.bool]),
        ),
        PropTypes.func,
        PropTypes.object,
    ]),
};

function LogoBox(props) {
    const { sx, ...other } = props;
    return (
        <Box
            sx={{
                my: 2,
                mx: '5%',
                display: 'flex',
                height: {xs: 30, sm: 40, lg: 60},
                justifyContent: 'center',
                ...sx,
            }}
            {...other}
        />
    );
}

LogoBox.propTypes = {
    /**
     * The system prop that allows defining system overrides as well as additional CSS styles.
     */
    sx: PropTypes.oneOfType([
        PropTypes.arrayOf(
            PropTypes.oneOfType([PropTypes.func, PropTypes.object, PropTypes.bool]),
        ),
        PropTypes.func,
        PropTypes.object,
    ]),
};

export default function Body(props) {
    return (
        <Box sx={{ display: 'flex', justifyContent: 'center' }} >
            <Box component="main"
                sx={{
                    width: {xs: '90%', sm:'90%', md: '80%', lg: '70%'},
                    mt: 4,
                    mb: 4,
                    mx: {xs: 1, sm: 2, md: 3, lg: 4},
                }}
            >
                <Toolbar />
                <Box
                    sx={{
                        display: 'flex',
                        justifyContent: 'center',
                    }}
                >
                    <div>
                        <Typography variant="h4" align="center" sx={{ fontWeight: 'bold' }}>
                            Habitat Synthetic Scenes Dataset (HSSD-200)
                        </Typography>
                        <Typography variant="h5" align="center" sx={{ fontWeight: 'bold' }}>
                            An Analysis of 3D Scene Scale and Realism Tradeoffs for ObjectGoal Navigation
                        </Typography>
                    </div>
                </Box>
                <Box
                    sx={{
                        display: 'flex',
                        justifyContent: 'center',
                        width: '100%',
                    }}
                >
                    <Box
                        component="img"
                        sx={{
                            display: 'flex',
                            width: '100%',
                            justifyContent: 'center',
                            my: 5
                        }}
                        alt="teaser"
                        src={teaser}
                    />
                </Box>
                <Box sx={{ display: 'grid', justifyContent: 'center'}}>
                    <Typography align="left" sx={{ typography: {xs: 'body', md: 'body', 'lg': 'h6'} }}>
                        We contribute the Habitat Synthetic Scenes Dataset
                        (HSSD-200), a dataset of 211 high-quality 3D scenes, and
                        use it to test navigation agent generalization to realistic 3D
                        environments. Our dataset represents real interiors and con-
                        tains a diverse set of 18,656 models of real-world objects.
                        We investigate the impact of synthetic 3D scene dataset scale
                        and realism on the task of training embodied agents to find
                        and navigate to objects (ObjectGoal navigation). By compar-
                        ing to synthetic 3D scene datasets from prior work, we find
                        that scale helps in generalization, but the benefits quickly
                        saturate, making visual fidelity and correlation to real-world
                        scenes more important. Our experiments show that agents
                        trained on our smaller-scale dataset can match or outper-
                        form agents trained on much larger datasets. Surprisingly,
                        we observe that agents trained on just 122 scenes from our
                        dataset outperform agents trained on 10,000 scenes from the
                        ProcTHOR-10K dataset in terms of zero-shot generalization
                        in real-world scanned environments.
                    </Typography>
                    <Header>Dataset</Header>
                    <Header>Results</Header>
                    <Header>Code</Header>
                    <Header>Team</Header>
                    <Box
                        sx={{
                            display: 'flex',
                            justifyContent: 'center',
                            alignItems: 'center'
                        }}
                    >
                        <LogoBox
                            component="img"
                            alt="georgia_logo"
                            src={georgia_logo}
                        />
                        <LogoBox
                            component="img"
                            alt="sfu_logo"
                            src={sfu_logo}
                        />
                        <LogoBox
                            component="img"
                            alt="stanford_logo"
                            src={stanford_logo}
                        />
                        <LogoBox
                            component="img"
                            sx={{
                                height: {xs: 15, sm: 20, lg: 30},
                            }}
                            alt="meta_logo"
                            src={meta_logo}
                        />
                    </Box>
                </Box>
            </Box>
        </Box>
    );
}